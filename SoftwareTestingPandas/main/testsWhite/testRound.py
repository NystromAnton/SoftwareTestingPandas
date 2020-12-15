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
    # TODO byt så det inte är cats o dogs som i deras exempel
    def setUp(self):      
        np.random.seed(25)
        self.df = pd.DataFrame(np.random.random([3, 4]), columns =["A", "B", "C", "D"]) 
       

    def testFirst(self):
        df = pd.DataFrame([(.239, .532), (.265, .982), (.902, .347), (.128, .298)], columns=['dogs', 'cats'])        
        df = df.round(1)    
        for column in df.iteritems():  
            for value in column[1].values:           
                self.assertEqual(str(value)[::-1].find('.'), 1)


    def testDict(self): #TODO Den kollar bara att det är en decimal men den bort också kolla att för cats är det bara nollor som decimal
        df = pd.DataFrame([(.21, .32), (.01, .67), (.66, .03), (.21, .18)], columns=['dogs', 'cats'])
        #print(df)      
        df = df.round({'dogs': 1, 'cats': 0}) 
        #print(df)
        for column in df.iteritems():  
            for value in column[1].values:           
                self.assertEqual(str(value)[::-1].find('.'), 1)

    def testSeries(self): #Det här testet adderade rad 8061 och 8062 
        """
        Tests using a series to specify different number of decimal places
        for different columns. Done by indexing by column names and decimal places as values.   

        Tests that values not of type integer or float gets returned as is without rounding. 
        """        
        df = pd.DataFrame([(.21, .32), (.01, .67), (.66, .03), (.21, .18)], columns=['dogs', 'cats'])      
        decimals = pd.Series([0, 1], index=['cats', 'dogs'])         
        df = df.round(decimals)          
        for column in df.iteritems():  #TODO Den kollar bara att det är en decimal men den bort också kolla att för cats är det bara nollor som decimal
            for value in column[1].values:           
                self.assertEqual(str(value)[::-1].find('.'), 1)
       
        df2 = pd.DataFrame([('val1', 'val2'), ('val3', 'val4'), ('val5', 'val6'), ('val7', 'val8')], columns=['col1', 'col2'])
        decimals2 = pd.Series([0, 1], index=['col1', 'col2'])        
        df3 = df.round(decimals2) # This ads rows 8049-8050    
        df4 = df2.round(decimals2) # This ads row 8055


    def stestForValueNotIntegerOrFloat(self):
        df = pd.DataFrame([("foo", .32), (.01, .67), (.66, .03), (.21, .18)], columns=['dogs', 'cats'])
        
        decimals = pd.Series([0, 1], index=['dogs', 'cats'])                 
        df = df.round(decimals)
        print(df)

    def testErrors(self):
        """
        Asserts that not unique indexing raises ValueError.
        Asserts that decimals not of type integer, dict-like or Series raises TypeError
        Ass
        """
        df = pd.DataFrame([(.21, .32), (.01, .67), (.66, .03), (.21, .18)], columns=['dogs', 'cats'])
        
        decimals = pd.Series([0, 1], index=['cats', 'cats'])         
        with self.assertRaises(ValueError):
            df = df.round(decimals)

        decimals = "string"
        with self.assertRaises(TypeError):
            df = df.round(decimals)       
           

    def testOneDecimal(self):
        data = self.df
        print(data)            
        data = data.round(1)          
        print(data)
        for column in data.iteritems():  
            for value in column[1].values:           
                self.assertEqual(str(value)[::-1].find('.'), 1)


    def testTwoDecimals(self):
        data = self.df        
        data = data.round(2)               
        for column in data.iteritems():  
            for value in column[1].values:                       
                self.assertTrue(str(value)[::-1].find('.') <= 2)


    def testMoreDecimals(self): 
        data = self.df     
        print(data)   
        data = data.round(8)  
        print(data)             
        for column in data.iteritems():  
            for value in column[1].values:        
                if str(value)[::-1].find('.') == 1:
                    print(value)
                    self.assertEqual(str(value)[-1], '0')  
                else:        
                    print(value)     
                    self.assertTrue(str(value)[::-1].find('.') <= 8)


    def testNoArgument(self): 
        data = self.df        
        data = data.round()               
        for column in data.iteritems():              
            for value in column[1].values:                                      
                if str(value)[::-1].find('.') == 1:
                    self.assertEqual(str(value)[-1], '0')
                else:  
                    self.assertTrue(str(value)[::-1].find('.') == 8)
    

    
if __name__ == '__main__' :    
    unittest.main()