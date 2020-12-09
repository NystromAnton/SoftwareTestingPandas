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
        self.df = pd.DataFrame({'col1': [1.2340303, 0.203, 9.0000], 'col2': [3.43245, 4.0, 288.349983], 'col3': [3.45, 4.52345, 4.002348937], 'col4': [3.4335, 4.55, 87.34829]})
       

    def testOneDecimal(self):
        data = self.df            
        data = data.round(1)          
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