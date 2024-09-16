import unittest
from rendlargent.main import rend_l_argent

class MyTestCase(unittest.TestCase):
    def test_1(self):
        compte_en_banque = rend_l_argent(8, 10)
        self.assertEqual(compte_en_banque, 18)

    def test_2(self):
        compte_en_banque = rend_l_argent(12, 10)
        self.assertEqual(compte_en_banque, 24)

if __name__ == '__main__':
    unittest.main()
