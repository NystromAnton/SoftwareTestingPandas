import unittest
import numpy as np
import pandas as pd
'''
Course: Software Testing
Team Number: 10
Author:
        Martin Dannelind (mada0115@student.uu.se)
Contributors:
        Julia Ekman (juek2660@student.uu.se)    
        Helena Frestadius (hefr3736@student.uu.se)
        Mette Nordqvist (meno5557@student.uu.se)
        Anton Nyström (anny0532@student.uu.se)
'''

'''
This file contains multiple white box tests for the function head from the library Pandas. 

Return the first n rows of a dataframe. This function returns the first n rows for the object based on position. 
It is useful for quickly testing if your object has the right type of data in it.
For negative values of n, this function returns all rows except the last n rows, equivalent to df[:-n].
'''
class TestPandasHead(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    def test1(self):
        data = self.df.head(1)
        print(data)
        dataComp = self.df.iloc[:1]
        print(dataComp)
        self.assertTrue(data.equals(dataComp))

if __name__ == '__main__' :
    unittest.main()