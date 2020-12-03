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
This file contains multiple black box tests for the function DataFrame.mean() from the library Pandas. 

The mean function computes the mean of a the vaules from a requested axis. 
'''
class TestPandasTitanic(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')
        
    #General case and with negative values
    def test1(self):
        self.assertEqual(self.df['Age'].mean(), 29.471443066516347)
        
        self.df['Age'] = -self.df['Age']
        self.assertEqual(self.df['Age'].mean(),-29.471443066516347)
        
        self.df['Age'] = 0
        self.assertEqual(self.df['Age'].mean(), 0)

    
    # Tests both values of axis, i.e. axis='index' (=0) and axis='columns'(=1)
    def test2(self):
        self.assertEqual(self.df['Age'].mean(axis=0), 29.471443066516347)
        
        self.assertEqual(self.df.mean(axis=1).iloc[0],5.541666666666667)
        
        with self.assertRaises(ValueError): 
            self.df['Age'].mean(axis=1)
        

    # With nan-values inserted in the column, using the default value of skipna=True
    def test3(self):
        self.df['Age'][0]= np.nan
        self.df['Age'][self.df.index[-1]]= np.nan
        self.assertEqual(self.df['Age'].mean(skipna=True), 29.47702824858757)

    # skipna = False
    def test4(self):
        self.df['Age'][0]= np.nan
        self.df['Age'][self.df.index[-1]]= np.nan
        self.assertEqual(pd.isnull(self.df['Age'].mean(skipna = False)), True)

    # Mean of column with only nan-values
    def test5(self):
        self.df['nan']= np.nan
        self.assertEqual(pd.isnull(self.df['nan'].mean()), True)

    # setting level in a multiindex axis.
    def test6(self):
        idx = pd.MultiIndex.from_arrays([
            ['sweet', 'sweet', 'sweet', 'salty', 'salty'],
            ['candy', 'cake', 'fruit','chips', 'french fries']],
            names=['taste', 'snack'])
        col = ['calories'] 
        x = pd.DataFrame([225, 430, 100, 350,370], idx, col)

        x=x.mean(level='taste')
        x=x.iloc[0]['calories']
        self.assertEqual(x, 251.66666666666666)

    # numeric_only=True and throw exception when numeric_only=False
    def test7(self):
        x = self.df.mean(numeric_only=True)
        self.assertEqual(x.iloc[0], 0.3855693348365276)
       
        with self.assertRaises(TypeError):
            self.df.mean(numeric_only=False)

    # TypeError
    def test8(self):
        with self.assertRaises(TypeError):
            self.df['Name'].mean()


if __name__ == '__main__' :
    unittest.main()
