"""Challenge #2."""
import unittest
from os.path import isfile


class TestIPInfoCreation(unittest.TestCase):
    """Test if IPInfo class is correctly imported."""

    def setUp(self):
        """Set up class variables."""
        self.class_file = 'modules/ipinfo.py'
        self.class_string = 'class IPInfo'

    def test_ipinfo_class_presence(self):
        """Test if Class IPInfo inside ipinfo.py is present."""
        self.assertTrue(isfile)
        with open(self.class_file) as rdata:
            module_contents = rdata.read()
        self.assertIn(self.class_string, module_contents)


class TestIncludeInit(unittest.TestCase):
    """Test if module ipinfo is included in __init__.py."""

    def setUp(self):
        """Set up class variables."""
        self.init_module = 'modules/__init__.py'
        self.module = 'IPInfo'
        self.import_line = 'from .ipinfo import IPInfo'
        self.all_special_method = f"__all__ = ['{self.module}']"

    def test_init_inclusion(self):
        """Test if modules are included in __init__.py."""
        with open(self.init_module, 'r') as rdata:
            init_contents = rdata.read()
        self.assertIn(self.import_line, init_contents,
                      msg="You haven't import IPInfo in __init__.py")
        self.assertIn(self.all_special_method, init_contents,
                      msg="__all__ is not defined in __init__.py")


if __name__ == '__main__':
    unittest.main()
