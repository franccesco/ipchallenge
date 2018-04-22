"""Challenge #5."""

import unittest
import modules


class TestIPInfoMethod1(unittest.TestCase):
    """Test IPInfo's documentation."""

    def setUp(self):
        """Set up test variables."""
        self.test_ip = '8.8.8.8'
        self.ip_info = modules.IPInfo(self.test_ip)

    def test_documentation(self):
        """Test class and method documentation."""
        self.assertIsInstance(modules.__doc__, str)
        self.assertIsInstance(modules.ipinfo.__doc__, str)
        self.assertIsInstance(self.ip_info.__doc__, str)
        self.assertIsInstance(self.ip_info.__init__.__doc__, str)
        self.assertIsInstance(self.ip_info.__repr__.__doc__, str)
        self.assertIsInstance(self.ip_info.__iter__.__doc__, str)
