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
        self.assertTrue(loads(self.ip_info.jsonify()))

    def test_2_to_file(self):
        """Test if data is dumped to file."""
        # dump to a file and check if it was created
        self.ip_info.to_file(self.file_dump, indent=4)
        self.assertTrue(isfile(self.file_dump))

        # check if file json compatible and finally remove it
        with open(self.file_dump) as robject:
            json_data = robject.read()
        self.assertTrue(loads(json_data))
        remove(self.file_dump)
