"""Tests for the utility functions"""
# -*- coding: utf-8 -*-
from unittest import TestCase
from ddt import ddt, data, unpack
from os import path
from utilities import check_input_strings, perform_proximity_search, \
    lower_unicode, make_index_directory, delete_index_directory, log_debug
from constants import TEST_BLOCK1, TEST_BLOCK2, EMPTY, TEST_DIRECTORY, \
    STRING_TYPE, UNICODE_TYPE, SEARCH1, SEARCH2, SEARCH3, \
    SEARCH4, DEFAULT_PROXIMITY, NEIGHBOR_PROXIMITY, \
    MISSING_PARAMETER_EXCEPTION, PARAMETER_EXCEPTION, SEARCH_TEST_DATA_LOG


@ddt
class UtilityMethodTests(TestCase):
    """Tests for the utility functions"""
    @unpack
    @data((TEST_BLOCK1, TEST_BLOCK2, EMPTY))
    def test_check_input_strings(self, string1, string2, string3):
        """Test the checking of invalid input"""
        self.assertTrue(check_input_strings(string1))
        self.assertTrue(check_input_strings(string1, string2))
        with self.assertRaises(type(MISSING_PARAMETER_EXCEPTION)):
            check_input_strings()
        with self.assertRaises(type(PARAMETER_EXCEPTION)):
            check_input_strings(string3)
        with self.assertRaises(type(PARAMETER_EXCEPTION)):
            check_input_strings(string1, string2, string3)

    @data(TEST_DIRECTORY)
    def test_index_directory(self, test_directory):
        """Test index directory methods"""
        if path.exists(test_directory):
            delete_index_directory(test_directory)
        self.assertFalse(path.exists(test_directory))
        make_index_directory(test_directory)
        self.assertTrue(path.exists(test_directory))
        delete_index_directory(test_directory)
        self.assertFalse(path.exists(test_directory))

    @unpack
    @data((TEST_BLOCK1, STRING_TYPE, UNICODE_TYPE))
    def test_unicode_conversion(self, test_value, string_type, unicode_type):
        """Test unicode conversion"""
        value = test_value
        self.assertEquals(str(type(value)), string_type)
        result = lower_unicode(value)
        self.assertEquals(str(type(result)), unicode_type)

    @unpack
    @data((TEST_BLOCK1, SEARCH1, DEFAULT_PROXIMITY, True),
          (TEST_BLOCK1, SEARCH2, DEFAULT_PROXIMITY, True),
          (TEST_BLOCK1, SEARCH1, NEIGHBOR_PROXIMITY, False),
          (TEST_BLOCK1, SEARCH3, NEIGHBOR_PROXIMITY, True),
          (TEST_BLOCK2, SEARCH2, DEFAULT_PROXIMITY, False),
          (TEST_BLOCK1, SEARCH4, DEFAULT_PROXIMITY, False))
    def test_proximity_search(
            self, text_block, search_terms, proximity, expected):
        """Test the proximity search function"""
        log_debug(SEARCH_TEST_DATA_LOG.format(
            text=text_block, search_terms=search_terms,
            proximity=proximity, expected=expected))
        result = perform_proximity_search(text_block, search_terms, proximity)
        self.assertEquals(result, expected)
