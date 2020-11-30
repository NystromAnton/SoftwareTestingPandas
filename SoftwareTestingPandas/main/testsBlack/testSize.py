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
This file contains multiple black box tests for the function size() from the library Pandas. 

Return an int representing the number of elements in this object. Return the number of rows if Series. Otherwise return the number of rows times number of columns if DataFrame.
In this test, only a dataframe is used.  
'''
class TestPandasTitanic(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """
      
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')
        self.emptydf = pd.DataFrame()
        self.nandf = pd.DataFrame({'col1': [np.NaN, np.NaN], 'col2': [np.NaN, np.NaN]})
        self.onenandf = pd.DataFrame({'col1': [1, 2], 'col2': [np.NaN, 4]})
    '''
    Test1 compares the regular output when the dataset is applied to the size function. It tests the basic funtionality of size(). 
    The input is the dataset called "df".
    The output should be equal to 7096. 
    '''         
    def test1(self):
        self.assertEqual(self.df.size,7096)

    '''
    Test2 checks if the size of an empty dataframe is equal to zero. 
    The input is called "emptydf" and is an empty dataset. 
    The output should be equal to zero. 
    '''
    def test2(self):
        self.assertEqual(self.emptydf.size, 0)

    '''
    Test3 checks if the size fuction works for NaN values in a dataset.  
    '''
    def test3(self):
        self.assertEqual(self.nandf.size, 4)
        self.assertEqual(self.onenandf.size, 4)

    '''
    Test4 makes sure the function throws an error in an the function is called with an input parameter.   
    '''
    def test4(self):
        data = self.df
        with self.assertRaises(TypeError):
            data.size(1)

if __name__ == "__main__": 
    unittest.main() 