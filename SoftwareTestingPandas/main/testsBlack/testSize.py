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

    def testSizeOriginal(self):
        self.assertEqual(self.df.size,7096)

if __name__ == '__main__' :
    unittest.main()