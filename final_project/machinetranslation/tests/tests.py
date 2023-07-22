import unittest
from translator import english_to_french, french_to_english
class TestStringMethods(unittest.TestCase):
    def test_words(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    
if __name__ == '__main__':
    unittest.main()