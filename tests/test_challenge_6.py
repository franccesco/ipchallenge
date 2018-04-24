"""Challenge 6."""

import unittest
from modules import IPInfo


class TestIPException(unittest.TestCase):
    """Test Exception if an invalid IP is passed."""

    def setUp(self):
        """Set up test variables."""
        self.invalid_ip = 'google.com'

    def test_exception(self):
        """Test if exception is catched."""
        with self.assertRaises(OSError):
            IPInfo(self.invalid_ip)
