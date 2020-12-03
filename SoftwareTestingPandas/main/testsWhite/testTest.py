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
This file contains multiple white box tests for the function '..' from the library Pandas.

The function '..' does the following....
'''
class TestPandasTitanic(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """

    def setUp(self):
        self.funcNone = lambda s1, s2: None
        self.df = pd.read_csv ('../src/data/titanic.csv')

    #def testTitanic(self):
    #    self.assertEqual(self.df.empty,False)

    #def testTitanic2(self):
    #    self.assertEqual(len(self.df.index),887)

    def testTitaniCombineW1(self):
        self.emptydf = pd.DataFrame()
        #print(self.df.combine(self.emptydf, self.funcNone))
        #print(self.emptydf)
        self.assertTrue(self.emptydf.combine(self.df, self.funcNone).equals(self.df))
        #self.assertTrue(self.df.combine(self.emptydf, self.funcNone).equals(self.emptydf))

if __name__ == '__main__' :
    unittest.main()
