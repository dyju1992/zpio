__author__ = 'dyju'

import unittest
import main

class Test_Wynik(unittest.TestCase):

    def test_sum_squares(self):
        self.assertEqual(main.Wynik[5], 13)


suite = unittest.TestLoader().loadTestsFromTestCase(Test_Wynik)
unittest.TextTestRunner(verbosity=2).run(suite)
