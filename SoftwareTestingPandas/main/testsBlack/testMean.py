import unittest
import numpy as np
import pandas as pd
'''
Course: Software Testing
Team Number: 10
Author:
        Helena Frestadius (hefr3736@student.uu.se)
Contributors: 
        Martin Dannelind (mada0115@student.uu.se)
        Julia Ekman (juek2660@student.uu.se)    
        Mette Nordqvist (meno5557@student.uu.se)
        Anton Nyström (anny0532@student.uu.se)
'''

'''
This file contains multiple black box tests for the function '..' from the library Pandas. 

The function '..' does the following....
'''
class TestPandasTitanic(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    def testMean(self):
        self.assertEqual(self.df['Age'].mean(), 29.471443066516347)


if __name__ == '__main__' :
    unittest.main()
