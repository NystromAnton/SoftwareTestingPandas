import unittest
import numpy as np
import pandas as pd
'''
Course: Software Testing
Team Number: 10
Author:
        Martin Dannelind (mada0115@student.uu.se)
        Julia Ekman (juek2660@student.uu.se)    
        Helena Frestadius (hefr3736@student.uu.se)
        Mette Nordqvist (meno5557@student.uu.se)
        Anton Nyström (anny0532@student.uu.se)
'''

'''
This file contains multiple white box tests for the function combine from the library Pandas. 

Combines a DataFrame with other DataFrame using func to element-wise combine columns. 
The row and column indexes of the resulting DataFrame will be the union of the two.
'''
class TestPandasGroupby(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')
        self.dfSurvived = self.df.groupby(by=['Survived']).size()
        self.dfSex = self.df.groupby(by=['Sex']).size()
        self.func = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
        self.funcSum = lambda s1, s2: s1.sum() + s2.sum()
        self.funcBad = lambda s1, s2: s1+None

    def testNoArgument(self):
        with self.assertRaises(TypeError):
            result = self.df.combine()        
    
    def testOneArgument(self):
        with self.assertRaises(TypeError):
            result = self.df.combine(self.dfSurvived)        

    def testBadFunc(self):
        with self.assertRaises(TypeError):
            result = self.df.combine(self.df, self.funcBad)        

    def test1(self):
        result = self.dfSurvived.combine(self.dfSurvived, self.funcSum)
        print(result)

if __name__ == '__main__' :
    unittest.main()