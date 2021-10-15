import unittest

from translator import english_to_french
from translator import french_to_english

class TestString(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"),"Bonjour") 
    def test2(self): 
        self.assertEqual(french_to_english("Bonjour"),"Hello") 
    def test3(self): 
        self.assertNotEqual(french_to_eglish("null"),"Hello") 
    def test4(self): 
        self.assertNotEqual(english_to_french("null"),"Bonjour")  

unittest.main()