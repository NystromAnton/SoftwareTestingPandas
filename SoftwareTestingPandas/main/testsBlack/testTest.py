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

<<<<<<< HEAD
=======

    def testMean(self):
        self.assertEqual(self.df['Age'].mean(), 29.471443066516347)


>>>>>>> f9e09b780f976b29936d43066da69c2d424a5253
if __name__ == '__main__' :
    unittest.main()
