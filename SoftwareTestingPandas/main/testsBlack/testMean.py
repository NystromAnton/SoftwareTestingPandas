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
This file contains multiple black box tests for the function DataFrame.mean() from the library Pandas. 

The mean function computes the mean of a the vaules from a requested axis. 
'''
class TestPandasTitanic(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    #General case 
    def test1(self):
        self.assertEqual(self.df['Age'].mean(), 29.471443066516347)

    #With nan as first value
    def test2(self):
        self.df['Age'][0]= np.nan
        self.assertEqual(self.df['Age'].mean(), 29.479875846501127)

    #With nan as first and last value
    def test3(self):
        self.df['Age'][0]= np.nan
        self.df['Age'][self.df.index[-1]]= np.nan
        self.assertEqual(self.df['Age'].mean(), 29.47702824858757)

    #mean of column with only nan and skipna = False
    def test4(self):
        self.df['nan']= np.nan
        self.assertFalse(self.df['nan'].mean(skipna=False) == np.nan)

    #TypeError
    def test5(self):
        with self.assertRaises(TypeError):
            self.df['Name'].mean()
    
    #test with negative values
    def test6(self):
        self.df['Age'] = -self.df['Age']
        self.assertEqual(self.df['Age'].mean(),-29.471443066516347)


if __name__ == '__main__' :
    unittest.main()
