"""Challenge #8."""

import unittest
from os import remove
from json import loads
from os.path import isfile
from modules import IPInfo


class TestIPModules(unittest.TestCase):
    """Test Three IPInfo Modules."""

    def setUp(self):
        """Initialize test variables."""
        self.file_dump = 'data.out'
        self.test_ip = '8.8.8.8'
        self.ip_info = IPInfo(self.test_ip)

    def test_1_jsonify(self):
        """Test if module Jsonify module returns a jsonified dictionary."""
        jsonified_str = self.ip_info.jsonify()
        self.assertTrue(loads(jsonified_str))
        self.assertEqual(len(jsonified_str.split('\n')), 1,
                         msg="Your jsonify method is indenting by default.")

    def test_2_to_file(self):
        """Test if data is dumped to file."""
        # dump to a file and check if it was created
        self.ip_info.to_file(self.file_dump)
        self.assertTrue(isfile(self.file_dump))

        # check if file json compatible and finally remove it
        with open(self.file_dump) as robject:
            json_data = robject.read()
        self.assertTrue(loads(json_data))
        remove(self.file_dump)

    def test_3_identation(self):
        """Test if jsonified data is indented."""
        jsonified_str = self.ip_info.jsonify(indent=4)
        self.assertIn(' ' * 4, jsonified_str)

    def test_4_file_indentation(self):
        """Test if file output is indented."""
        self.ip_info.to_file(self.file_dump, indent=4)
        with open(self.file_dump, 'r') as rdata:
            jsonified_str = rdata.read()
        self.assertIn(' ' * 4, jsonified_str)
