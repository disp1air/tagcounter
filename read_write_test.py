import unittest
import read_write
from unittest.mock import MagicMock

class WorkWithDBTestCase(unittest.TestCase):
    def test_write_data_to_db_called(self):
        read_write.write_data_to_db = MagicMock()
        read_write.work_with_db("ya.ru", "--get")
        read_write.write_data_to_db.assert_called_once_with("ya.ru")

    def test_read_data_from_db_called(self):
        read_write.read_data_from_db = MagicMock()
        read_write.work_with_db("ya.ru", "--view")
        read_write.read_data_from_db.assert_called_once_with("ya.ru")

    def test_functions_not_called(self):
        read_write.write_data_to_db = MagicMock()
        read_write.read_data_from_db = MagicMock()
        read_write.work_with_db("ya.ru", "--gget")
        assert not read_write.write_data_to_db.called
        assert not read_write.read_data_from_db.called

unittest.main()