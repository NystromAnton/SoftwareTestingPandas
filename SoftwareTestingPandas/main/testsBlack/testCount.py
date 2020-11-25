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
This file contains multiple black box tests for the function DataFrame.count() from the library Pandas.

The function DataFrame.count() counts the number of elements that are != NaN
'''
class TestPandasTitanic(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """

    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    #def testTitanic(self):
        #self.assertEqual(self.df.empty,False)

    #def testTitanic2(self):
        #df = pd.read_csv ('../src/data/titanic.csv')
        #self.assertEqual(len(self.df.index),887)

    def testTitanicCount1(self):
        self.df['Survived'].replace(0, np.nan, inplace = True)
        self.df['Survived'].replace(1, np.nan, inplace = True)
        self.assertEqual(self.df['Survived'].count(), 0)

    def testTitanicCount2(self):
        self.assertEqual(self.df['Name'].count(), 887)

    def testTitanicCount3(self):
        self.assertEqual(self.df.loc[self.df.Survived == 1, 'Survived'].count(), 342)

    def testTitanicCount4(self):
        self.df['Fare'].replace(0, np.nan, inplace = True)
        self.assertEqual(self.df['Fare'].count(), 872)

    def testTitanicCount5(self):
        self.df['Fare'].replace(0, np.nan, inplace = True)
        dict = {'Name' : self.df['Name'], 'Fare' : self.df['Fare']}
        self.df = pd.DataFrame(dict)
        self.assertTrue(self.df.count().equals(pd.Series({"Name" : 887 , "Fare" : 872})))




if __name__ == '__main__' :
    unittest.main()
