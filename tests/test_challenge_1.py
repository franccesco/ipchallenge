"""Challenge #1."""
import unittest
from os.path import isdir, isfile


class TestModules(unittest.TestCase):
    """Test Module Creation."""

    def setUp(self):
        """Set up class variables."""
        self.modules_dir = 'modules/'
        self._init = '__init__.py'
        self.ip_class = 'ipinfo.py'

    def test_create_module_folder(self):
        """Test the project architecture"""
        # test if 'modules/' folder was created.
        self.assertTrue(isdir(self.modules_dir),
                        msg="Directory 'modules' is missing")

        # test if __init.py__ is under the 'modules/' directory.
        self.assertTrue(isfile(self.modules_dir + self._init),
                        msg="The file __init__.py was not found in'modules/'")
        self.assertTrue(isfile(self.modules_dir + self.ip_class),
                        msg="The file ipinfo.py was not found in'modules/'")
        print('Challenge #1 was a success!')
        print('Please proceed with Challenge #2\n')


if __name__ == '__main__':
    unittest.main()
