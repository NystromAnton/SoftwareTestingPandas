import unittest
import numpy as np
import pandas as pd
'''
Course: Software Testing
Team Number: 10    
Contributors: 
        Julia Ekman (juek2660@student.uu.se)    
        Helena Frestadius (hefr3736@student.uu.se)
        Mette Nordqvist (meno5557@student.uu.se)
        Anton Nyström (anny0532@student.uu.se)
        Martin Dannelind (mada0115@student.uu.se)
'''

'''
This file contains multiple black box tests for the function "pop" from the Pandas library. 

A pop operation returns a specified column and drops it from the dataframe. Raises a KeyError if column not found.
'''
class TestPandasPop(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    def testSize(self):   
        data = self.df
        noColumns = len(data.columns)
        data.pop("Pclass")
        self.assertEqual(noColumns-1, len(data.columns))
        
        data.pop("Survived")
        data.pop("Age")
        data.pop("Fare")
        self.assertEqual(noColumns-4, len(data.columns))

    def testRemoved(self):
        data = self.df       
        self.assertIn("female", data.values)
        self.assertIn("male", data.values)        
        self.assertIn("Miss. Ellen O'Dwyer", data.values)

        data.pop("Sex")    
        self.assertNotIn("female", data.values)
        self.assertNotIn("female", data.values)
        self.assertNotIn("male", data.values)
        self.assertIn("Miss. Ellen O'Dwyer", data.values)

    def testNoArgument(self):
        data = self.df
        with self.assertRaises(TypeError):
            data.pop()            

    def testInvalidArgument(self):
        data = self.df    
        with self.assertRaises(NameError):
            data.pop(argumentWithoutQuotation)
        
    def testColumnNotFound(self):
        data = self.df
        with self.assertRaises(KeyError):
            data.pop("")
        
        with self.assertRaises(KeyError):
            data.pop("Boattype")

    
if __name__ == '__main__' :
    unittest.main()
