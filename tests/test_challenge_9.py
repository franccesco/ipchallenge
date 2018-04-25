"""Challenge 9."""
import unittest
from os.path import isfile
from io import StringIO
from subprocess import run
from contextlib import redirect_stdout
from modules import IPInfo


class TestIPInfoCodeReview(unittest.TestCase):
    """Test modules code quality."""

    def setUp(self):
        """Initialize test variables."""
        self.hook = '.git/hooks/pre-commit'
        self.test_ip = '8.8.8.8'
        self.ip_info = IPInfo(self.test_ip)

    def test_flake8(self):
        text_trap = StringIO()
        with redirect_stdout(text_trap):
            run("pipenv run flake8 .", shell=True, check=True)

    def test_flake8_hook(self):
        """Test if flake8 hook was initialized."""
        self.assertTrue(isfile(self.hook), msg='No pre-commit hook detected.')
