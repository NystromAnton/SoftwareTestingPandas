import unittest
import numpy as np
import pandas as pd
'''
Course: Software Testing
Team Number: 10
Author:
        Mette Nordqvist (meno5557@student.uu.se)
Contributors:
        Martin Dannelind (mada0115@student.uu.se)
        Julia Ekman (juek2660@student.uu.se)
        Helena Frestadius (hefr3736@student.uu.se)
        Anton Nyström (anny0532@student.uu.se)
'''

'''
This file contains multiple black box tests for the function DataFrame.count()
from the library Pandas.

The function DataFrame.count() counts the number of elements that are != NaN
in a DataFrame and returns an intager.
'''

class TestPandasTitanicCountB(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """

    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

        # Replacing all of the values in the first column with Nan values
        # and testing that the function to be tested returns 0
    def testTitanicCountB1(self):
        self.df['Survived'].replace(0, np.nan, inplace = True)
        self.df['Survived'].replace(1, np.nan, inplace = True)
        self.assertEqual(self.df['Survived'].count(), 0)

    # Counts all names in the 'Name' column
    def testTitanicCountB2(self):
        self.assertEqual(self.df['Name'].count(), 887)

    # Counts all of the survivers
    def testTitanicCountB3(self):
        self.assertEqual(self.df.loc[self.df.Survived == 1, 'Survived'].count(), 342)

    # All values in the 'Fare' column that are equal to 0 are replaced by NaN values
    # and then that column is counted
    def testTitanicCountB4(self):
        self.df['Fare'].replace(0, np.nan, inplace = True)
        self.assertEqual(self.df['Fare'].count(), 872)

    # Again replaces all 0 values in the 'Fare' column with NaN.
    # Then counts the 'Fare' column as well as the 'Name' column
    # And return a Series datatype
    def testTitanicCountB5(self):
        self.df['Fare'].replace(0, np.nan, inplace = True)
        dict = {'Name' : self.df['Name'], 'Fare' : self.df['Fare']}
        self.df = pd.DataFrame(dict)
        count = pd.DataFrame(dict).count();
        self.assertTrue(self.df.count().equals(pd.Series({"Name" : 887 , "Fare" : 872})))

        '''
        Name    887
        Fare    872
        dtype: int64

        '''

    # Again replaces all 0 values in the 'Fare' column with NaN.
    # This case tests the parameter axis is set to 'index'.
    # This will count the number of elements in every column
    # And return a Series datatype
    def testTitanicCountB6(self):
        self.df['Fare'].replace(0, np.nan, inplace = True)
        self.assertTrue(self.df.count(axis = 'index').equals(pd.Series([887, 887, 887,
        887, 887, 887, 887, 872], ['Survived', 'Pclass', 'Name', 'Sex', 'Age',
        'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare'])))

        '''
        Survived                   887
        Pclass                     887
        Sex                        887
        Age                        887
        Siblings/Spouses Aboard    887
        Parents/Children Aboard    887
        Fare                       872
        dtype: int64
        '''

    # This case tests the parameter level is set to 'Pclass'.
    # This test counts the number of names and divides them into three groups
    # depending on which class they were travelling in
    def testTitanicCountB7(self):
        countPclass = self.df.set_index(['Survived','Pclass', 'Sex', 'Age','Siblings/Spouses Aboard',
        'Parents/Children Aboard', 'Fare']).count(level = 'Pclass')
        self.assertTrue(countPclass.at[1, 'Name'] == 216)
        self.assertTrue(countPclass.at[2, 'Name'] == 184)
        self.assertTrue(countPclass.at[3, 'Name'] == 487)
        '''
                Name
        Pclass
        1        216
        2        184
        3        487
        '''

if __name__ == '__main__' :
    unittest.main()
