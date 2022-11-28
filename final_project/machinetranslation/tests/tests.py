import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F (unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench('Hello'), None)
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestF2E (unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'), None)
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")    

unittest.main()
