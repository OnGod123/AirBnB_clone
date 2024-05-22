import unittest
from unittest.mock import mock_open, patch
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_content = json.dumps({
            "BaseModel.123": {
                "id": "123",
                "created_at": "2024-01-01T12:00:00.000000",
                "updated_at": "2024-01-01T12:00:00.000000"
            }
        })

    def test_save(self):
        with patch('builtins.open', mock_open()) as mock_file:
            fs = FileStorage()
            obj = BaseModel(id="123", created_at="2024-01-01T12:00:00.000000", updated_at="2024-01-01T12:00:00.000000")
            fs.new(obj)
            fs.save()
            mock_file.assert_called_once_with('file.json', 'w')
            mock_file().write.assert_called_once_with(self.file_content)

    def test_reload(self):
        with patch('builtins.open', mock_open(read_data=self.file_content)):
            fs = FileStorage()
            fs.reload()
            obj = fs.all()["BaseModel.123"]
            self.assertEqual(obj.id, "123")
            self.assertEqual(obj.created_at.isoformat(), "2024-01-01T12:00:00.000000")
            self.assertEqual(obj.updated_at.isoformat(), "2024-01-01T12:00:00.000000")

if __name__ == "__main__":
    unittest.main()

