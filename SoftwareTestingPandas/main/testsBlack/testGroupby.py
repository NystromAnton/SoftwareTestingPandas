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
This file contains multiple black box tests for the function groupby from the library Pandas. 

A groupby operation involves some combination of splitting the object, applying a function, and combining the results. 
This can be used to group large amounts of data and compute operations on these groups.
'''
class TestPandasTitanic(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    def testSurvived(self):
        data = self.df.groupby(['Survived']).size()
        self.assertEqual(data[0],545)
        self.assertEqual(data[1],342)
        """
        Survived
        0    545
        1    342
        dtype: int64
        """

    def testSex(self):
        data = self.df.groupby(['Sex']).size()
        self.assertEqual(data[0],314)
        self.assertEqual(data[1],573)
        """
        Sex
        female    314
        male      573
        dtype: int64
        """

if __name__ == '__main__' :
    unittest.main()
