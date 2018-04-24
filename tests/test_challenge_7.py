"""Challenge 7."""

import unittest
from modules import IPInfo


class TestIPCustomException(unittest.TestCase):
    """Test Custom Exception Message."""

    def setUp(self):
        """Set up test variables."""
        self.invalid_ip = 'google.com'

    def test_custom_exception(self):
        """Test if exception has a custom messaged."""
        with self.assertRaises(ValueError) as err:
            IPInfo(self.invalid_ip)
        exception_msg = str(err.exception)
        self.assertEqual(exception_msg, 'Invalid IP Address.')
