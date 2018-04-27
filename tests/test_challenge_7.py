"""Challenge 7."""

import unittest
import traceback
from modules import IPInfo


class TestIPCustomException(unittest.TestCase):
    """Test Custom Exception Message."""

    def setUp(self):
        """Set up test variables."""
        self.invalid_ip = 'google.com'

    def test_1_custom_exception(self):
        """Test if exception has a custom messaged."""
        with self.assertRaises(ValueError) as err:
            IPInfo(self.invalid_ip)
        exception_msg = str(err.exception)
        self.assertEqual(exception_msg, 'Invalid IP Address.')

    def test_2_chained_exception(self):
        """Test if test is chained."""
        message = ("\n\nThere were two exceptions raised. This happens if you "
                   "raise another ValueError(message) in your code. "
                   "Try changing the arguments of the exception "
                   "instead of rasing *another* exception.\n"
                   "Go ahead and load your module to a python interpreter "
                   "and feed your class with an invalid IP to test it out. "
                   "There should be only _one_ exception, not two of them.")
        try:
            IPInfo(self.invalid_ip)
        except ValueError:
            tb = traceback.format_exc()
        self.assertNotIn('During handling', tb, msg=message)
