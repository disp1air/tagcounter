import unittest
import requests
from tagcounter import main
from requests import Response
from unittest.mock import MagicMock
from bs4 import BeautifulSoup

class TagcounterTestCase(unittest.TestCase):
    def test_tagcounter(self):
        response = Response()
        response.text = MagicMock(return_value="<div>123</div>")
        requests.get = MagicMock(return_value=response.text)
        result = main()
        self.assertEqual(result, {"div": 1})

unittest.main()