import unittest
from check_synonyms import check_synonyms

class checkSynonymsTestCase(unittest.TestCase):
    def test_check_synonyms(self):
        result = check_synonyms("ya")
        self.assertEqual(result, "ya.ru")

        result = check_synonyms("onl")
        self.assertEqual(result, "onliner.by")

        result = check_synonyms("github")
        self.assertEqual(result, "github")

        result = check_synonyms("google")
        self.assertEqual(result, "google")

unittest.main()
