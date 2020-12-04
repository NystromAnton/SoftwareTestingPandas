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
This file contains multiple white box tests for the function DataFrame.count() from the library Pandas.

The function DataFrame.count() counts the number of elements that are != NaN
in a DataFrame and returns an intager.
'''
class TestPandasTitanicCountW(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """

    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')
        self.dfempty = pd.DataFrame()
        first = [1, 2, 3]
        second = [4, 5, 6]
        numeric = {"first":first, "second":second}
        self.dfintegers = pd.DataFrame(numeric)

    # This case tests the parameter level is set to 'Pclass'.
    # This test counts the number of names and divides them into three groups
    # depending on which class they were travelling in
    def testTitanicCountW1(self):
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
    # Changing the numeric_only parameter to True while the axis is set to 'index'
    # returns a Series that counts the number of elements in each column where all
    # of the values are of type integer, float or boolean
    def testTitanicCountW2(self):
        self.assertTrue(self.df.count(axis = 'index', numeric_only=True).equals(pd.Series([887,
        887, 887, 887, 887, 887], ['Survived', 'Pclass', 'Age',
        'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare'])))
        '''
        Survived                   887
        Pclass                     887
        Age                        887
        Siblings/Spouses Aboard    887
        Parents/Children Aboard    887
        Fare                       887
        dtype: int64
        '''

    # Again replaces all 0 values in the 'Fare' column with NaN.
    # This case tests the parameter axis is set to 'index'.
    # This will count the number of elements in every column
    # And return a Series datatype
    def testTitanicCountW3(self):
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

    # Using an empty DataFrame to count while the axis is set to index
    # Returns an empty Series of dtype int64
    def testEmptyDFW5(self):
        self.assertTrue(self.dfempty.count(axis = 'index').equals(pd.Series([]).astype('int64')))
        '''
        first     3
        second    3
        dtype: int64
        '''

    # By using a DataFrame that only consists of numeric values e.g. no mixed
    # types and no extention types I can access the else statement on row 8471
    def testIntegersOnlyW4(self):
        print(self.dfintegers.count(axis = 'index'))
        self.assertTrue(self.dfintegers.count(axis = 'index').equals(pd.Series([3, 3], ['first', 'second'])))

if __name__ == '__main__':
    unittest.main()
