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
        self.df = pd.DataFrame({\
            'col1': [decimal.Decimal('1.2340303'), decimal.Decimal('0.203'), decimal.Decimal('9.0000')], \
            'col2': [decimal.Decimal('3.43245'), decimal.Decimal('4.0'), decimal.Decimal('288.349983')], \
            'col3': [decimal.Decimal('3.45'), decimal.Decimal('4.52345'), decimal.Decimal('4.002348937')], \
            'col4': [decimal.Decimal('3.4335'), decimal.Decimal('4.55'), decimal.Decimal('87.34829')]})
       

    def testFirst(self):
        df = pd.DataFrame([(.21, .32), (.01, .67), (.66, .03), (.21, .18)], columns=['dogs', 'cats'])        
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

        # This added rows 8049 and 8050
        df2 = pd.DataFrame([('val1', 'val2'), ('val3', 'val4'), ('val5', 'val6'), ('val7', 'val8')], columns=['col1', 'col2'])
        decimals2 = pd.Series([0, 1], index=['col1', 'col2'])
        print(df2)
        df2 = df2.round(decimals2)
        print(df2)


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
           

    def stestOneDecimal(self):
        data = self.df
        print(data)            
        data = data.round(1)          
        print(data)
        for column in data.iteritems():  
            for value in column[1].values:           
                self.assertEqual(str(value)[::-1].find('.'), 1)


    def stestTwoDecimals(self):
        data = self.df        
        data = data.round(2)               
        for column in data.iteritems():  
            for value in column[1].values:                       
                self.assertTrue(str(value)[::-1].find('.') <= 2)


    def stestMoreDecimals(self): 
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


    def stestNoArgument(self): 
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