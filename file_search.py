"""Searches files for search terms"""
# -*- coding: utf-8 -*-
from os import walk, path
from utilities import log_debug, log_info, log_error, check_input_strings
from word_search import WordSearch
from constants import OPEN_READ, FILE_LOG_MESSAGE, FILE_NAME_INDEX, \
    DIRECTORY_LOG_MESSAGE, FILE_CONTENT_LOG_MESSAGE, \
    FILE_RESULT_LOG_MESSAGE, DIRECTORY_RESULT_LOG_MESSAGE, DEFAULT_PROXIMITY


class FileSearch(object):
    """File search class that searches single file or files in directory"""
    def __init__(self, word_search=None):
        """Initialization method with dependencies optionally passed"""
        self._word_search = word_search or WordSearch()

    def search_file(self, file_path, search_terms,
                    proximity=DEFAULT_PROXIMITY):
        """Search a single file for search criteria"""
        try:
            check_input_strings(file_path, search_terms)
            log_debug(FILE_LOG_MESSAGE.format(file=file_path))
            file_object = open(file_path, OPEN_READ)
            file_contents = file_object.read()
            log_info(FILE_CONTENT_LOG_MESSAGE.format(text=file_contents))
            search_result = self._word_search.perform_search(
                file_contents, search_terms, proximity)
            log_debug(FILE_RESULT_LOG_MESSAGE.format(
                file=file_path, result=search_result))
            return search_result
        except ValueError as ex:
            log_error(ex)
            return None

    def search_files_in_directory(self, directory_location, search_terms,
                                  proximity=DEFAULT_PROXIMITY):
        """Search all txt files in directory for the passed search criteria"""
        matching_files = list()
        try:
            check_input_strings(directory_location, search_terms)
            if not path.exists(directory_location):
                return matching_files
            log_debug(DIRECTORY_LOG_MESSAGE.format(
                directory=directory_location))
            files = [path.join(directory_location, file_name) for
                     file_name in next(walk(directory_location))
                     [FILE_NAME_INDEX]]
            for file_name in files:
                result = self.search_file(file_name, search_terms, proximity)
                if result:
                    matching_files.append(file_name)
            log_debug(DIRECTORY_RESULT_LOG_MESSAGE.format(
                directory=directory_location, result=matching_files))
            return matching_files
        except ValueError as ex:
            log_error(ex)
            return None
