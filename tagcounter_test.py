import unittest
import responses
import tagcount
from unittest.mock import MagicMock

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    def __getattr__(self, name):
        return self[name]

class TagcounterTestCase(unittest.TestCase):
    @responses.activate
    def test_tagcounter_1(self):
        responses.add(responses.GET, "https://ya.ru", json={'error': "not found"},
            status=404)
        
        test_dict = dotdict({})
        test_dict.name = "div"

        tagcount.BeautifulSoup = MagicMock()
        tagcount.BeautifulSoup().findAll = MagicMock(return_value=[test_dict])
        
        result = tagcount.tag_count("ya.ru")
        self.assertEqual(result, {"div": 1})
        
    @responses.activate
    def test_tagcounter_2(self):
        responses.add(responses.GET, "https://ya.ru", json={'error': "not found"},
            status=404)
        
        test_dict1 = dotdict({})
        test_dict1.name = "div"

        test_dict2 = dotdict({})
        test_dict2.name = "ul"

        test_dict3 = dotdict({})
        test_dict3.name = "div"

        tagcount.BeautifulSoup = MagicMock()
        tagcount.BeautifulSoup().findAll = MagicMock(return_value=[test_dict1, test_dict2, test_dict3])
        
        result = tagcount.tag_count("ya.ru")
        self.assertEqual(result, {"div": 2, "ul": 1})
        
unittest.main()
