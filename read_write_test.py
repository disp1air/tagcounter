import unittest
from read_write import work_with_db
from unittest.mock import MagicMock
from data import read_data_from_db, write_data_to_db

class WorkWithDBTestCase(unittest.TestCase):
    def test_work_with_db(self):
        write_data_to_db = MagicMock()
        work_with_db("ya.ru", "--get")
        assert write_data_to_db.called
unittest.main()