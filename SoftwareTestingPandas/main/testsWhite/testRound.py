import unittest
import numpy as np
import pandas as pd
import decimal
'''
Course: Software Testing
Team Number: 10
Author:
        Anton Nyström (anny0532@student.uu.se)
Contributors:
        Martin Dannelind (mada0115@student.uu.se)
        Julia Ekman (juek2660@student.uu.se)    
        Helena Frestadius (hefr3736@student.uu.se)
        Mette Nordqvist (meno5557@student.uu.se)        
'''

'''
This file contains multiple white box tests for the function round from the library Pandas. 

Round rounds a DataFrame to a variable number of decimal places. 
By providing an integer each column is rounded to the same number of decimal places.
With a dict, the number of places for specific columns can be specified with the column names as key
    and the number of decimal places as value.
Using a Series, the number of places for specific columns can be specified with the column names as index 
    and the number of decimal places as value.

'''
class TestPandasRound(unittest.TestCase):

    def setUp(self):      
        np.random.seed(120)
        self.df = pd.DataFrame(np.random.random([3, 4]), columns =["1", "2", "3", "4"]) 
       

    def testInt(self):
        """
        Tests that specifying an int as argument rounds value to that amount of decimals
        """
        df = pd.DataFrame([(.239, .532), (.265, .982), (.902, .347), (.128, .298)], columns=['col1', 'col2'])        
        df = df.round(1)    
        for column in df.iteritems():  
            for value in column[1].values:           
                self.assertEqual(str(value)[::-1].find('.'), 1)

        data = self.df               
        dataRounded2 = data.round(2)                    
        for column in dataRounded2.iteritems():  
            for value in column[1].values:                          
                self.assertTrue(str(value)[::-1].find('.') <= 2)
        
        dataRounded5 = data.round(5)          
        for column in dataRounded5.iteritems():  
            for value in column[1].values:        
                self.assertTrue(str(value)[::-1].find('.') <= 5)
    

    def testDict(self):
        """
        Tests using a dict to specify different number of decimal places
        for different columns. Done by having column name as key and decimal places as value.    
        """
        df = pd.DataFrame([(.239, .532), (.265, .982), (.902, .347), (.128, .298)], columns=['col1', 'col2'])        
        df = df.round({'col1': 1, 'col2': 0})   
        listOfValues = []  
        for column in df.iteritems():  
            for value in column[1].values:      
                listOfValues.append(value)
                self.assertEqual(str(value)[::-1].find('.'), 1)

        for x in range(0,4):
            value = str(listOfValues[x])
            self.assertTrue(value.startswith('0.'))
            self.assertFalse(value.endswith('.0'))

        for x in range(4,8):            
            value = str(listOfValues[x])           
            self.assertTrue(value.endswith('.0'))              


    def testSeries(self):
        """
        Tests using a series to specify different number of decimal places
        for different columns. Done by indexing by column names and decimal places as values.       
        """        
        df = pd.DataFrame([(.239, .532), (.265, .982), (.902, .347), (.128, .298)], columns=['col1', 'col2'])     
        decimals = pd.Series([0, 1], index=['col2', 'col1'])         
        df = df.round(decimals)          
        for column in df.iteritems():
            for value in column[1].values:           
                self.assertEqual(str(value)[::-1].find('.'), 1)

        for value in df['col1']:
            valueCopy = str(value)
            self.assertTrue(valueCopy.startswith('0.'))
            self.assertFalse(valueCopy.endswith('.0'))
        
        for value in df['col2']:
            valueCopy = str(value)
            self.assertTrue(valueCopy.endswith('.0'))
               
        
    def testKeyErrorIndexing(self):
        """
        Tests that faulty indexing which makes program catch a KeyError results in return of DataFrame unchanged. 
        """
        df = pd.DataFrame([(.239, .532), (.265, .982), (.902, .347), (.128, .298)], columns=['col1', 'col2'])
        decimals2 = pd.Series([0, 1], index=['A', 'B'])           
        dfKeyError = df.round(decimals2) # This ads rows 8049-8050                      
        self.assertTrue(df.equals(dfKeyError))  


    def testValueNotIntOrFloat(self):
        """
        Tests that supplying values not of type integer or float returns DataFrame unchanged.
        """
        df = pd.DataFrame([('val1', 'val2'), ('val3', 'val4'), ('val5', 'val6'), ('val7', 'val8')], columns=['A', 'B'])
        decimals = pd.Series([0, 1], index=['A', 'B'])
        dfRounded = df.round(decimals)     # Row 8055
        self.assertTrue(df.equals(dfRounded))         


    def testDifferingColumn(self):
        """
        Tests that if a column contains one value not of type integer or float, 
        then no other value in that column gets rounded. The other columns should be rounded.
        """
        df = pd.DataFrame([("foo", .323), (.0413, .677), (.6566, .083), (.2791, .118)], columns=['col1', 'col2'])
        decimals = pd.Series([6, 2], index=['col1', 'col2'])                 
        dfRounded = df.round(decimals)

        self.assertTrue(df['col1'].equals(dfRounded['col1']))
        self.assertFalse(df['col2'].equals(dfRounded['col2'])) 
        for value in dfRounded['col2'].values:           
                self.assertEqual(str(value)[::-1].find('.'), 2)    


    def testErrors(self):
        """
        Asserts that not unique indexing raises ValueError.
        Asserts that decimals not of type integer, dict-like or Series raises TypeError       
        """
        df = pd.DataFrame([(.239, .532), (.265, .982), (.902, .347), (.128, .298)], columns=['col1', 'col2'])
        
        decimals = pd.Series([0, 1], index=['col2', 'col2'])         
        with self.assertRaises(ValueError): # 8061 and 8062
            df = df.round(decimals)

        decimals = "string"
        with self.assertRaises(TypeError):
            df = df.round(decimals)                  

   
    def testNoArgument(self): 
        """
        Tests that not supplying an argument to round() results in float-value getting 
        rounded to closest integer.
        """
        data = self.df              
        data = data.round()            

        for column in data.iteritems():              
            for value in column[1].values:                                                          
                self.assertEqual(str(value)[-1], '0')                                
                self.assertTrue(str(value).startswith('0') or str(value).startswith('1'))                    

    
if __name__ == '__main__' :    
    unittest.main()