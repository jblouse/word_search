"""Constants for the search algorithms"""
# -*- coding: utf-8 -*-
import logging
from os.path import expanduser

MAIN_NAME = '__main__'
OPEN_READ = 'r'
FILE_NAME_INDEX = 2
EMPTY = ''
STRING_TYPE = "<type 'str'>"
UNICODE_TYPE = "<type 'unicode'>"
TEST_DIRECTORY = 'YO_TEST'
TEST_BLOCK1 = 'this is a stupid simple text block'
TEST_BLOCK2 = 'this is a simple block of text'
TEST_BLOCK3 = 'this is a third test block of \ntext.' \
              '\n\n\nplease find the next word'
SEARCH1 = 'stupid text'
SEARCH2 = 'stupid'
SEARCH3 = 'stupid simple'
SEARCH4 = 'dumb'
SEARCH5 = 'this test'
SEARCH6 = 'find word'
SEARCH7 = 'this the'
TEST_FILES_DIRECTORY = 'test_files'
TEST_FILE1 = 'test1.txt'
TEST_FILE2 = 'test2.txt'
TEST_FILE3 = 'test3.txt'
PARAMETER_ERROR = 'Invalid input parameter(s)'
MISSING_PARAMETER_ERROR = 'Missing input parameter(s)'
MISSING_PARAMETER_EXCEPTION = ValueError(MISSING_PARAMETER_ERROR)
PARAMETER_EXCEPTION = ValueError(PARAMETER_ERROR)
INDEX_DIR_NAME = '_indices_'
DECODER = 'utf-8'
CONTENT_FIELD = 'content'
NEIGHBOR_PROXIMITY = 1
DEFAULT_PROXIMITY = 4
PROXIMITY_QUERY = '"{search_terms}"~{proximity}'
LOG_FILE_PATH = 'search_debug.log'
LOG_LEVEL = logging.DEBUG
logging.basicConfig(filename=LOG_FILE_PATH, level=LOG_LEVEL)

DIRECTORY_LOG_MESSAGE = 'Searching .txt files in {directory}...'
FILE_CONTENT_LOG_MESSAGE = 'File Contents\n-------------------\n{text}'
FILE_LOG_MESSAGE = 'Searching file {file}...'
SEARCH_RESULT_MESSAGE = 'Search result: {result}'
SEARCH_LOG_MESSAGE = 'Searching for {terms} in *****{text}*****'
FILE_RESULT_LOG_MESSAGE = '{file} search result: {result}...'
DIRECTORY_RESULT_LOG_MESSAGE = '{directory} search results: {result}...'
SEARCH_TEST_DATA_LOG = 'Testing data: Text: {text} ---- Search: ' \
                       '{search_terms} ---- Proximity: {proximity} ' \
                       '---- Expected: {expected}'
DEFAULT_DIRECTORY = expanduser('./tests/test_files')
DIRECTORY_QUESTION = \
    'Enter the full directory path you wish to search[{directory}]: '.format(
        directory=DEFAULT_DIRECTORY)
DEFAULT_SEARCH = 'try search'
SEARCH_QUESTION = 'Enter your search criteria. ' \
                  'Use 1 for exact match[{search}]: '.format(
                      search=DEFAULT_SEARCH)
PROXIMITY_QUESTION = 'Enter the word context proximity[{proximity}]: '.format(
    proximity=DEFAULT_PROXIMITY)
RESULT_SUMMARY = 'The following files match your search criteria...'
ERROR_MESSAGE_USER = 'Something bad happened. Inspect {log} ' \
                     'for more detailed information.'.format(log=LOG_FILE_PATH)
