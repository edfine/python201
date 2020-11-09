from services import RemovalService, UploadService
from unittest import mock
import unittest

class UploadServiceTestCase(unittest.TestCase):

    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # when we create a RemovealService object...
        # ...the rm method will automatically be mocked
        removal_service = RemovalService()
        
        ref = UploadService(removal_service)
        
        # call upload_complete, which should, in turn, call `rm`:
        ref.upload_complete("my uploaded file")
        
        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")
        
        # check that it called the rm method of _our_ removal_service
        removal_service.rm.assert_called_with("my uploaded file")

unittest.main()

