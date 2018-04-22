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
        self.assertIsInstance(modules.__doc__, str,
                              msg="__init__.py lacks documentation")
        self.assertIsInstance(modules.ipinfo.__doc__, str,
                              msg="ipinfo.py lacks top documentation")
        self.assertIsInstance(self.ip_info.__doc__, str,
                              msg="class IPInfo lacks documentation.")
        self.assertIsInstance(self.ip_info.__init__.__doc__, str,
                              msg="Init method in class lacks documentation")
        self.assertIsInstance(self.ip_info.__repr__.__doc__,
                              str, msg="Class repr lacks documentation.")
        self.assertIsInstance(self.ip_info.__iter__.__doc__,
                              str, msg="Iteration method lacks documentation.")
