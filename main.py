#!/usr/bin/env python
"""Main python script module"""
from file_search import FileSearch
from constants import DIRECTORY_QUESTION, DEFAULT_DIRECTORY, \
    SEARCH_QUESTION, DEFAULT_SEARCH, PROXIMITY_QUESTION, \
    DEFAULT_PROXIMITY, RESULT_SUMMARY, MAIN_NAME, ERROR_MESSAGE_USER


def main():
    """Wrapper script to request input and call the search routine"""
    try:
        directory_path = raw_input(DIRECTORY_QUESTION) or DEFAULT_DIRECTORY
        search_criteria = raw_input(SEARCH_QUESTION) or DEFAULT_SEARCH
        context_proximity = raw_input(PROXIMITY_QUESTION) or DEFAULT_PROXIMITY
        file_search = FileSearch()
        matching_files = file_search.search_files_in_directory(
            directory_path, search_criteria, int(context_proximity))
        print RESULT_SUMMARY
        if matching_files is None:
            print ERROR_MESSAGE_USER
            return
        for match in matching_files:
            print match
    except IOError:
        print ERROR_MESSAGE_USER


if __name__ == MAIN_NAME:
    main()
