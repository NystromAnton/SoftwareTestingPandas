import unittest
import numpy as np
import pandas as pd
'''
Course: Software Testing
Team Number: 10
Author:
        Julia Ekman (juek2660@student.uu.se)
Contributors:
        Martin Dannelind (mada0115@student.uu.se)
        Helena Frestadius (hefr3736@student.uu.se)
        Anton Nyström (anny0532@student.uu.se)
        Mette Nordqvist (meno5557@student.uu.se)
'''

'''
This file contains multiple white box tests for the function DataFrame.dot() from the library Pandas.

This method computes the matrix product between the DataFrame and the values of an other Series, DataFrame or a numpy array.
'''
class TestPandasTitanicCountW(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')
        self.dfempty = pd.DataFrame()
        self.wrongDim = pd.DataFrame()
       
    # This test makes sure that the function throws an error when run on two dataframes with different dimensions. 
    def testIncorrectDimensions(self):
        d1 = {'col1': [1, 2], 'col2': [3, 4]}
        d2 = {'col1': [1], 'col2': [3]}
        frame1 = pd.DataFrame(data=d1)
        frame2 = pd.DataFrame(data=d2)
        with self.assertRaises(ValueError):
            frame1.dot(frame2)
    
    #This test makes sure the function raises an ValueError for shape mismatch. 
    def testShapeMismatch(self):
        d1 = {'col1': [1], 'col2': [3]}
        frame1 = pd.DataFrame(data=d1)
        a = (1,2,3) 
        b = (1,3)     
        with self.assertRaises(ValueError):
            frame1.dot(a)

        self.assertTrue(frame1.dot(b).equals(pd.Series([10],[0])))
          
    #This test checks that the dot function works as expected the the input is a dataframe. Tests that it works for a 4 by 4 matrix filled with ints and empty matrixes. 
    def testDataFrame(self):
        df = pd.DataFrame([[0, 1, -2, -1], [1, 1, 1, 1]])
        other = pd.DataFrame([[0, 1], [1, 2], [-1, -1], [2, 0]])
        result1 = df.dot(other)
        d4 = {'0': [1, 2], '1': [4, 2]}
        frame3 = pd.DataFrame(data=d4)
        self.assertTrue(np.array_equal(result1, frame3))
        result2 = self.dfempty.dot(self.dfempty)
        self.assertTrue(np.array_equal(self.dfempty, result2))
    
    #This test checks that the function works as expected for a Series. One of the matrices is a DataFrame, and the other is a Series.  
    def testSeries(self):
        serie = pd.Series([1, 1, 2, 1])
        df = pd.DataFrame([[0, 1, -2, -1], [1, 1, 1, 1]])
        result = df.dot(serie)
        rvals = [[1,2,3,4], [3,6,2,5]]
        lvals = [[1,2], [3,6], [3,6], [6,8]]
        result2 = np.dot(rvals, lvals)
        self.assertTrue(result2.ndim == 2)

if __name__ == '__main__':
    unittest.main()
