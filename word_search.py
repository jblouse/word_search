"""Class for searching blocks of text for matching terms"""
# -*- coding: utf-8 -*-
from utilities import check_input_strings, perform_proximity_search, log_debug
from constants import DEFAULT_PROXIMITY, SEARCH_LOG_MESSAGE, \
    SEARCH_RESULT_MESSAGE


class WordSearch(object):  # pylint: disable=too-few-public-methods
    """Search class for searching text blocks for search criteria"""
    def __init__(self, search_method=perform_proximity_search):
        """Default initializer"""
        self.search = search_method

    def perform_search(self, text_block, search_terms,
                       proximity=DEFAULT_PROXIMITY):
        """Search text block for search terms using search algorithm"""
        log_debug(SEARCH_LOG_MESSAGE.format(
            terms=search_terms, text=text_block))
        check_input_strings(text_block, search_terms)
        result = self.search(text_block, search_terms, proximity)
        log_debug(SEARCH_RESULT_MESSAGE.format(result=result))
        return result
