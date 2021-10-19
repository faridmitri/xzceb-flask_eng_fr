import unittest
from  translator import EnglishToFrench,FrenchToEnglish

class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(EnglishToFrench(''),'') # test when '' is given as input the output is ''.
        self.assertEqual(EnglishToFrench('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.

class TestFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(FrenchToEnglish(''),'') # test when '' is given as input the output is ''.
        self.assertEqual(FrenchToEnglish('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.