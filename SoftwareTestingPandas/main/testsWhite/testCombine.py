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
class TestPandasCombine(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')
        self.dfSurvived = self.df.groupby(by=['Survived']).size()
        self.dfSex = self.df.groupby(by=['Sex']).size()
        self.func = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
        self.funcSum = lambda s1, s2: s1.sum() + s2.sum()
        self.funcBad = lambda s1, s2: s1+None
        self.funcNone = lambda s1, s2: None
        self.take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2

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
        #print(result)

    def testTitaniCombineW1(self):
        self.emptydf = pd.DataFrame()
        #print(self.df.combine(self.emptydf, self.funcNone))
        #print(self.emptydf)
        self.assertTrue(self.emptydf.combine(self.df, self.funcNone).equals(self.df))
        #self.assertTrue(self.df.combine(self.emptydf, self.funcNone).equals(self.emptydf))

    def test1_2_5_6_7_8_10_11_12_13_17_18(self):
        newdf= pd.DataFrame({'a':[1,1], 'b':[None,3]})
        otherdf = pd.DataFrame({'b':[0.0,2.3], 'c':[None,4]})
        expecteddf= pd.DataFrame({'a':[np.NaN, np.NaN], 'b':[0.0, 2.3], 'c': [np.NaN, np.NaN]})
        self.assertTrue(newdf.combine(otherdf, self.take_smaller).equals(expecteddf))


    def test1_2_5_6_7_8_10_12_14_15_17_18(self):
        newdf= pd.DataFrame({'a':[1,1], 'b':[None,3]})
        otherdf = pd.DataFrame({'a':[0.0,2.3], 'b':[None,4]})
        expecteddf=pd.DataFrame({'a':[1, 1], 'b':[None, 3.0]})
        self.assertTrue(newdf.combine(otherdf, self.take_smaller).equals(expecteddf))
        

    #Common columnnames, value_fill is not none, different dtypes in dataframes, changes to the dtype of other
    def test1_2_5_6_7_8_10_11_12_14_15_17_18(self):
        newdf= pd.DataFrame({'a':[1,1], 'b':[None,3]})
        otherdf = pd.DataFrame({'a':[0.0,2.3], 'b':[None,4]})
        expecteddf=pd.DataFrame({'a':[1, 1], 'b':[-5.0, 3.0]})
        self.assertTrue(newdf.combine(otherdf, self.take_smaller, fill_value=-5).equals(expecteddf))

    #Common columnnames, value_fill is not none, different dtypes in dataframes, changes to the dtype of self
    def test1_2_5_6_7_8_10_11_12_14_16_17_18(self):
        newdf=pd.DataFrame({'a':[0.0,2.3], 'b':[None,4]})
        otherdf = pd.DataFrame({'a':[1,1], 'b':[None,3]})
        expecteddf=pd.DataFrame({'a':[1.0, 1.0], 'b':[-5.0, 3.0]})
        self.assertTrue(newdf.combine(otherdf, self.take_smaller, fill_value=-5).equals(expecteddf))


if __name__ == '__main__' :
    unittest.main()