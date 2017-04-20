"""Tests for the file search."""
# -*- coding: utf-8 -*-
from unittest import TestCase
from os.path import join, dirname, abspath
from inspect import getfile, currentframe
from ddt import ddt, data, unpack
from file_search import FileSearch
from constants import TEST_DIRECTORY, DEFAULT_SEARCH, \
    TEST_FILES_DIRECTORY, TEST_FILE1, SEARCH3, TEST_FILE3, \
    TEST_FILE2, SEARCH5, EMPTY


@ddt
class FileSearchTests(TestCase):
    """Tests for the FileSearch class"""
    @unpack
    @data((TEST_DIRECTORY, DEFAULT_SEARCH, 0),
          (TEST_FILES_DIRECTORY, SEARCH5, 3))
    def test_directory_search(self, test_directory, search_terms, expected):
        """Test searching a directory of files"""
        test_file_directory = dirname(abspath(getfile(currentframe())))
        test_directory = join(test_file_directory, test_directory)
        search = FileSearch()
        results = search.search_files_in_directory(
            test_directory, search_terms)
        self.assertEquals(len(results), expected)
        results = search.search_files_in_directory(EMPTY, EMPTY)
        self.assertIsNone(results)

    @unpack
    @data((TEST_FILE1, SEARCH3, False), (TEST_FILE2, SEARCH5, True),
          (TEST_FILE3, SEARCH3, False))
    def test_file_search(self, test_file, search_terms, expected):
        """Test the search for a single file"""
        search_directory = join(dirname(
            abspath(getfile(currentframe()))), TEST_FILES_DIRECTORY)
        search_file = join(search_directory, test_file)
        search = FileSearch()
        result = search.search_file(search_file, search_terms)
        self.assertEquals(result, expected)
        result = search.search_file(EMPTY, EMPTY)
        self.assertIsNone(result)
