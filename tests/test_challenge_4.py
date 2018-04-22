"""Challenge #4."""

import unittest
from modules import IPInfo


class TestIPInfoREPR(unittest.TestCase):
    """Test IPInfo's first method."""

    def setUp(self):
        """Set up test variables."""
        self.test_ip = '8.8.8.8'
        self.ip_info = IPInfo(self.test_ip)

    def test_repr(self):
        """Test if repr have a custom message."""
        self.assertEqual(
            f'Geolocation information of {self.test_ip}', repr(self.ip_info))
