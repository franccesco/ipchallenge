"""Challenge #3."""
import unittest
from json import dumps
from modules import IPInfo


class TestIPInfo(unittest.TestCase):
    """Test IPInfo module."""

    def setUp(self):
        """Set up test variables."""
        self.test_ip = '8.8.8.8'
        self.ip_info = IPInfo(self.test_ip)

    def test_ip_info_class_attributes_count(self):
        """Test attributes in self.class"""
        attribute_count = (len(self.ip_info.__dict__.keys()))
        self.assertEqual(attribute_count, 1,
                         msg="The'res more than one 'self.' in that class.")

    def test_if_ip_data_return_dictionary(self):
        """Test if self.ip_info.ip_data returns a JSON line."""
        self.assertIsInstance(self.ip_info.ip_data, dict,
                              msg="ip_data doesn't return a dict string.")
        self.assertTrue(dumps(self.ip_info.ip_data))
