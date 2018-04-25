"""Challenge #4."""

import unittest
from types import GeneratorType
from modules import IPInfo


class TestIPInfoREPR(unittest.TestCase):
    """Test IPInfo's Repr method."""

    def setUp(self):
        """Set up test variables."""
        self.test_ip = '8.8.8.8'
        self.ip_info = IPInfo(self.test_ip)

    def test_1_repr(self):
        """Test if repr have a custom message."""
        self.assertEqual(
            f'Geolocation information of {self.test_ip}', repr(self.ip_info))

    def test_2_iter(self):
        """Test iteration method."""
        self.assertIsInstance(iter(self.ip_info), GeneratorType)
        values = dict(val for val in self.ip_info)
        self.assertIsInstance(values, dict)
