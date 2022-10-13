from permissions_open import permissions_open
from unittest import mock
import unittest

class TestPermissionsOpen(unittest.TestCase):
    def test_permissions_open(self):
        with mock.patch('os.chmod') as chmod:
            permissions_open('/tmp/test.txt')
            chmod.assert_called_with('/tmp/test.txt', 0o777)
            chmod.assertTrue(chmod.called)
            chmod.assertEqual()

unittest.main()