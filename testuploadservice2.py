from services import RemovalService, UploadService
from unittest import mock
import unittest

class UploadServiceTestCase(unittest.TestCase):

    def test_upload_complete(self):
        # build our dependencies
        mock_removal_service = mock.create_autospec(RemovalService)
        ref = UploadService(mock_removal_service)
        
        # call upload_complete, which should, in turn, call `rm`:
        ref.upload_complete("my uploaded file")
        
        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")

unittest.main()

