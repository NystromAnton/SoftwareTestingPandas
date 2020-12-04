import unittest
import numpy as np
import pandas as pd

from pandas.core.dtypes.missing import isna, na_value_for_dtype, notna
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

Parameters:
other :: DataFrame
The DataFrame to merge column-wise.

func :: function
Function that takes two series as inputs and return a Series or a scalar. Used to merge the two dataframes column by columns.

fill_value :: scalar value, default None
The value to fill NaNs with prior to passing any column to the merge func.

overwrite :: bool, default True
If True, columns in self that do not exist in other will be overwritten with NaNs.
'''
class TestPandasCombine(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')
        self.dfDuplicates = self.df.drop(columns=['Name','Fare','Siblings/Spouses Aboard','Age'])
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

    def test1_2_4(self):
        self.emptydf = pd.DataFrame()
        #print(self.df.combine(self.emptydf, self.funcNone))
        #print(self.emptydf)
        self.assertTrue(self.emptydf.combine(self.df, self.funcNone).equals(self.df))
        #self.assertTrue(self.df.combine(self.emptydf, self.funcNone).equals(self.emptydf))

    def test1_2_3(self):
        d = {'col1': [None, None]}
        other = pd.DataFrame()
        d = {'col1': [1, 2], 'col2': [3, 4]}
        selfdf = pd.DataFrame()

        this, other = selfdf.align(other, copy=False) 
        new_index = this.index 
        self.assertTrue(other.empty)
        self.assertEqual(len(new_index), len(selfdf.index))

        data = selfdf.combine(other, self.funcNone)
        self.assertTrue(data.equals(selfdf.copy()))

    def test1_2_4(self):
        d = {'col1': [1, 2], 'col2': [3, 4]}
        other = pd.DataFrame(data=d)
        selfdf = pd.DataFrame()

        other_idxlen = len(other.index)
        this, other = selfdf.align(other, copy=False) 
        self.assertTrue(selfdf.empty)
        self.assertEqual(len(other), other_idxlen)

        data = selfdf.combine(other, self.funcNone)
        self.assertTrue(data.equals(other.copy()))

    def test1_2_5_6_7_8_9(self):
        take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
        selfdf = pd.DataFrame({'A': [0, 0], 'B': [4, 4], 'C':[None,None]})
        other = pd.DataFrame({'B': [3, 3], 'C': [None, None], 'D':[11,11], }, index=[1, 2])
        overwrite = False

        self.assertFalse(overwrite)

        other_idxlen = len(other.index)
        this, other = selfdf.align(other, copy=False) 
        new_index = this.index 

        self.assertNotEqual(len(new_index), len(selfdf.index))
        self.assertNotEqual(len(other), other_idxlen)

        data = selfdf.combine(other, take_smaller)
        
    def test1_2_5_6_7_8_10_12_13_17_18(self):
        newdf= pd.DataFrame({'a':[1.1,1.2], 'b':[3.1,4.3]})
        otherdf = pd.DataFrame({'b':[1,2], 'c':[3,4]})
        expecteddf = pd.DataFrame({'a':[np.NaN, np.NaN], 'b':[1.0,2.0], 'c':[np.NaN, np.NaN]})

        self.assertTrue(newdf.combine(otherdf, self.take_smaller).equals(expecteddf))


    def test1_2_5_6_7_8_10_11_12_13_17_18(self):
        newdf= pd.DataFrame({'a':[1,1], 'b':[None,3]})
        otherdf = pd.DataFrame({'b':[0.0,2.3], 'c':[None,4]})
        expecteddf= pd.DataFrame({'a':[-5, -5], 'b':[-5.0, 3.0], 'c': [-5.0, -5.0]})
        self.assertTrue(newdf.combine(otherdf, self.take_smaller, fill_value=-5.0).equals(expecteddf))

    def test1_2_5_6_7_8_10_12_14_15_17_18(self):
        newdf= pd.DataFrame({'a':[1,1], 'b':[None,3]})
        otherdf = pd.DataFrame({'a':[0.0,2.3], 'b':[None,4]})
        expecteddf=pd.DataFrame({'a':[1, 1], 'b':[None, 3.0]})
        self.assertTrue(newdf.combine(otherdf, self.take_smaller).equals(expecteddf))
        
    def test1_2_5_6_7_8_10_12_14_16_17_18(self):
        newdf=pd.DataFrame({'a':[0.0,2.3], 'b':[None,4]})
        otherdf = pd.DataFrame({'a':[1,1], 'b':[None,3]})
        expecteddf=pd.DataFrame({'a':[1.0, 1.0], 'b':[np.NaN, 3.0]})
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