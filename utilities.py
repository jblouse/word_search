"""Utility functions"""
# -*- coding: utf-8 -*-
from os import path, mkdir, rmdir
from logging import getLogger
from whoosh.fields import Schema, TEXT
from whoosh.index import create_in
from whoosh.qparser import QueryParser
from constants import DECODER, INDEX_DIR_NAME, DEFAULT_PROXIMITY, \
    CONTENT_FIELD, EMPTY, MISSING_PARAMETER_EXCEPTION, PARAMETER_EXCEPTION, \
    PROXIMITY_QUERY


def log_error(message):
    """Write error log message"""
    getLogger(__name__).exception(message)


def log_info(message):
    """Write info log message"""
    getLogger(__name__).info(message)


def log_debug(message):
    """Write debug log message"""
    getLogger(__name__).debug(message)


def lower_unicode(value):
    """Convert string to unicode using decoder"""
    return value.decode(DECODER).lower()


def check_input_strings(*values):
    """Raise a value error is parameter is an empty string"""
    if not values:
        raise MISSING_PARAMETER_EXCEPTION
    for value in values:
        if not value:
            raise PARAMETER_EXCEPTION
    return True


def make_index_directory(directory_name=INDEX_DIR_NAME):
    """Create a directory for storing index files"""
    check_input_strings(directory_name)
    if not path.exists(directory_name):
        mkdir(directory_name)


def delete_index_directory(directory_name=INDEX_DIR_NAME):
    """Delete the index directory"""
    check_input_strings(directory_name)
    if path.exists(directory_name):
        rmdir(directory_name)


def _get_index(text_block):
    """Get whoosh indexer"""
    make_index_directory()
    search_text = TEXT
    schema = Schema(content=search_text)
    index = create_in(INDEX_DIR_NAME, schema)
    writer = index.writer()
    writer.add_document(content=lower_unicode(text_block))
    writer.commit()
    return index


def perform_proximity_search(text_block, search_terms,
                             proximity=DEFAULT_PROXIMITY):
    """Search text block for search terms within proximity context"""
    index = _get_index(text_block)
    parser = QueryParser(CONTENT_FIELD, index.schema)
    query = PROXIMITY_QUERY.format(
        search_terms=search_terms, proximity=proximity)
    log_debug(query)
    query = parser.parse(query)
    with index.searcher() as searcher:
        results = searcher.search(query, terms=True)
        term_match = len(results) > len(EMPTY)
    return term_match
