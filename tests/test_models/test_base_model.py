#/usr/bin/env python3

import unittest
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test initialization of BaseModel."""
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime.datetime)
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

    def test_str(self):
        """Test string representation of BaseModel."""
        base_model = BaseModel()
        base_model_str = str(base_model)
        self.assertIn(base_model.__class__.__name__, base_model_str)
        self.assertIn(base_model.id, base_model_str)

    def test_to_dict(self):
        """Test conversion of BaseModel to dictionary."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    @patch('models.storage.new')
    @patch('models.storage.save')
    def test_save(self, mock_save, mock_new):
        """Test save method of BaseModel."""
        base_model = BaseModel()
        base_model.save()
        self.assertTrue(mock_new.called)
        self.assertTrue(mock_save.called)

if __name__ == '__main__':
    unittest.main()

