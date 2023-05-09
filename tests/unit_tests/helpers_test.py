'''This module performs Unit tests on the following directory: ./helpers/'''

import unittest
from pyaml_env import parse_config
from helpers import misc


class MiscTest(unittest.TestCase):
    '''Test the following file functions: ../misc.py'''

    def setUp(self):
        '''Configure test inputs.'''
        self.yaml_ = 'config.yaml'
        self.string = 'this,is,a,test,string,with,commas'
        self.lst = ['this', 'is', 'a', 'test', 'string', 'with', 'commas']
        self.db_url = 'postgres://username:password@host:port/database'
        self.db_url2 = 'postgresql://username:password@host:port/database'
        self.nested_list = [['test', 'list', '1'], ['test', 'list', '2']]
        self.unpacked_list = ['test', 'list', '1', 'test', 'list', '2']

    def tearDown(self):
        '''Reset test inputs.'''
        self.yaml_ = None
        self.string = None
        self.lst = None
        self.db_url = None
        self.db_url2 = None
        self.nested_list = None
        self.unpacked_list = None

    def test_time(self):
        '''Test the # Time section.'''
        self.assertIsInstance(misc.current_utc_timestamp(), int)

    def test_data_type(self):
        '''Test the # Data type convertion section.'''
        data = misc.string_to_list(self.string)
        self.assertIsInstance(data, list)
        self.assertListEqual(data, self.lst)

    def test_format(self):
        '''Test the # Formatting section.'''
        url = misc.format_db_url(self.db_url)
        self.assertIsInstance(url, str)
        self.assertEqual(url, self.db_url2)

        flat = misc.flatten_list(self.nested_list)
        self.assertIsInstance(flat, list)
        self.assertListEqual(flat, self.unpacked_list)

    def test_reading_file(self):
        '''Test if the following files exist and are readable.'''
        assert parse_config(path=self.yaml_)
