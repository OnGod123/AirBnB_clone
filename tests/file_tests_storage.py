import unittest
from unittest.mock import mock_open, patch
from your_module import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_content = '{"TestClass.123": {"id": "123", "name": "test"}}'
    
    def test_save(self):
        with patch('builtins.open', mock_open()) as mock_file:
            fs = FileStorage()
            fs.__objects = {'TestClass.123': {'id': '123', 'name': 'test'}}
            fs.save()
            mock_file.assert_called_once_with('file.json', 'w')
            mock_file().write.assert_called_once_with(self.file_content)
    
    def test_reload(self):
        with patch('builtins.open', mock_open(read_data=self.file_content)):
            fs = FileStorage()
            fs.reload()
            self.assertEqual(fs.__objects, {'TestClass.123': {'id': '123', 'name': 'test'}})

