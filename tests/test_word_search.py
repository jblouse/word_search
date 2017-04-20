"""Tests for the word search."""
# -*- coding: utf-8 -*-
from unittest import TestCase
from ddt import ddt, data, unpack
from mock import Mock
from word_search import WordSearch
from constants import TEST_BLOCK1, SEARCH1, SEARCH4, PARAMETER_EXCEPTION, \
    EMPTY, TEST_BLOCK3, SEARCH5, SEARCH6, SEARCH7


@ddt
class WordSearchTests(TestCase):
    """Tests for the WordSearch class"""
    def test_word_proximity_search(self):
        """Test proximity search which is default"""
        search = WordSearch()
        match = search.perform_search(TEST_BLOCK1, SEARCH1)
        self.assertTrue(match)
        with self.assertRaises(type(PARAMETER_EXCEPTION)):
            search.perform_search(TEST_BLOCK1, EMPTY)

    @unpack
    @data((TEST_BLOCK3, SEARCH5, True), (TEST_BLOCK3, SEARCH6, True),
          (TEST_BLOCK3, SEARCH7, False))
    def test_proximity_lines(self, test_block, search_terms, expected):
        """Test a search with words on multiple lines"""
        search = WordSearch()
        match = search.perform_search(test_block, search_terms)
        self.assertEquals(match, expected)

    @data(True, False)
    def test_passed_search(self, value):
        """Test mocked search methods"""
        mock_search = Mock(return_value=value)
        word_search = WordSearch(mock_search)
        result = word_search.perform_search(TEST_BLOCK1, SEARCH4)
        self.assertEquals(result, value)
