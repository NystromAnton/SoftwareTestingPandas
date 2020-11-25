import unittest
import numpy as np
import pandas as pd
'''
Course: Software Testing
Team Number: 10
Contributors:
        Martin Dannelind (mada0115@student.uu.se)
        Julia Ekman (juek2660@student.uu.se)
        Helena Frestadius (hefr3736@student.uu.se)
        Mette Nordqvist (meno5557@student.uu.se)
        Anton Nyström (anny0532@student.uu.se)
'''

'''
This file contains multiple black box tests for the function '..' from the library Pandas.

The function '..' does the following....
'''
class TestPandasTitanic(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """

    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    def testTitanic(self):
        self.assertEqual(self.df.empty,False)

    def testTitanic2(self):
        df = pd.read_csv ('../src/data/titanic.csv')
        self.assertEqual(len(self.df.index),887)

    def testTitanicCount(self):
        self.assertEqual(self.df.loc[self.df.Survived == 1, 'Survived'].count(), 342)


if __name__ == '__main__' :
    unittest.main()
