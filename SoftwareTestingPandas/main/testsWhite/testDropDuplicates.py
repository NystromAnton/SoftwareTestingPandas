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
This file contains multiple white box tests for the function drop_duplicates from the library Pandas. 

Return DataFrame with duplicate rows removed. Considering certain columns is optional. 
Indexes, including time indexes are ignored.
'''
class TestPandasDropDuplicates(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')
        self.dfDuplicates = self.df.drop(columns=['Name','Fare','Siblings/Spouses Aboard','Age'])

    def test1(self):
        """
        Test for empty dataframe
        """
        data = pd.DataFrame()
        self.assertTrue(data.empty)
        dataComp = data.drop_duplicates()
        self.assertTrue(data.equals(dataComp))

    def test2(self):
        """
        Test for unique and duplicate dataset
        """
        data = self.df.drop_duplicates()
        dataComp = self.df
        self.assertTrue(data.equals(dataComp))

        data = self.dfDuplicates.drop_duplicates()
        dataComp = self.dfDuplicates
        self.assertFalse(data.equals(dataComp))


    def test3(self):
        """
        Test for ignore_index parameter

        ignore_index :: bool, default False
        If True, the resulting axis will be labeled 0, 1, ..., n-1.
        """
        # Does not respond to none boolean value: BUG
        dataError = self.df.drop_duplicates(ignore_index='error')

        data = self.df.drop_duplicates(ignore_index=False)
        dataComp = self.df.drop_duplicates(ignore_index=True)
        self.assertTrue(data.equals(dataComp))

        data = self.dfDuplicates.drop_duplicates(ignore_index=False)
        dataComp = self.dfDuplicates.drop_duplicates(ignore_index=True)
        self.assertFalse(data.equals(dataComp))


        data = self.dfDuplicates.drop_duplicates(ignore_index=False)
        dataComp = self.dfDuplicates.drop_duplicates(ignore_index=set())
        self.assertTrue(data.equals(dataComp))

        data = self.dfDuplicates.drop_duplicates(ignore_index="")
        dataComp = self.dfDuplicates.drop_duplicates(ignore_index=None)
        self.assertTrue(data.equals(dataComp))

        data = self.dfDuplicates.drop_duplicates(ignore_index=list())
        dataComp = self.dfDuplicates.drop_duplicates(ignore_index=0)
        self.assertTrue(data.equals(dataComp))

        data = self.dfDuplicates.drop_duplicates(ignore_index=True)
        dataComp = self.dfDuplicates.drop_duplicates(ignore_index="True")
        self.assertTrue(data.equals(dataComp))


    def test4(self):
        """
        Test for inplace parameter

        inplace :: bool, default False
        Whether to drop duplicates in place or to return a copy.
        """
        with self.assertRaises(ValueError):
            dataError = self.df.drop_duplicates(inplace='error')

        data = self.df.drop_duplicates(inplace=False)
        dataComp = self.df.drop_duplicates(inplace=True)
        self.assertFalse(data.equals(dataComp))

        data = self.dfDuplicates.drop_duplicates(inplace=False)
        dataComp = self.dfDuplicates.drop_duplicates(inplace=True)
        self.assertFalse(data.equals(dataComp))

    def test5(self):
        """
        Test for keep parameter

        keep :: {‘first’, ‘last’, False}, default ‘first’
        Determines which duplicates (if any) to keep. 
        -first: Drop duplicates except for the first occurrence. 
        -last: Drop duplicates except for the last occurrence. 
        -False: Drop all duplicates.
        """
        with self.assertRaises(ValueError):
            dataError = self.df.drop_duplicates(keep='error')
        with self.assertRaises(ValueError):
            dataError = self.df.drop_duplicates(keep=None)


        dataFirst = self.df.drop_duplicates(keep='first')
        dataLast = self.df.drop_duplicates(keep='last')
        dataFalse = self.df.drop_duplicates(keep=False)
        self.assertTrue(dataFirst.equals(dataLast))
        self.assertTrue(dataFirst.equals(dataFalse))
        self.assertTrue(dataLast.equals(dataFalse))

        dataFirst = self.dfDuplicates.drop_duplicates(keep='first')
        dataLast = self.dfDuplicates.drop_duplicates(keep='last')
        dataFalse = self.dfDuplicates.drop_duplicates(keep=False)
        self.assertFalse(dataFirst.equals(dataLast))
        self.assertFalse(dataFirst.equals(dataFalse))
        self.assertFalse(dataLast.equals(dataFalse))


    def test6(self):
        """
        Test for subset parameter

        subset :: column label or sequence of labels, optional
        Only consider certain columns for identifying duplicates, by default use all of the columns.
        """ 
        with self.assertRaises(KeyError):
            dataError = self.df.drop_duplicates(subset=['error'])

        data = self.df.drop_duplicates()
        dataComp = self.df.drop_duplicates(subset=['Age'])
        self.assertFalse(data.equals(dataComp))

    def testValidateBoolKwarg(self):
        # Correct boolean value
        inplace = True
        self.assertTrue(pd.util._validators.validate_bool_kwarg(inplace, "inplace"))
        inplace = "True"
        with self.assertRaises(ValueError):
            self.assertTrue(pd.util._validators.validate_bool_kwarg(inplace, "inplace"))

        # Correct boolean value
        inplace = False
        self.assertFalse(pd.util._validators.validate_bool_kwarg(inplace, "inplace"))
        # For None no ValueError was raised as expected.
        inplace = None
        self.assertFalse(pd.util._validators.validate_bool_kwarg(inplace, "inplace"))

        inplace = ""
        with self.assertRaises(ValueError):
            self.assertFalse(pd.util._validators.validate_bool_kwarg(inplace, "inplace"))
        inplace = 0
        with self.assertRaises(ValueError):
            self.assertFalse(pd.util._validators.validate_bool_kwarg(inplace, "inplace"))
        inplace = set()
        with self.assertRaises(ValueError):
            self.assertFalse(pd.util._validators.validate_bool_kwarg(inplace, "inplace"))
        inplace = list()
        with self.assertRaises(ValueError):
            self.assertFalse(pd.util._validators.validate_bool_kwarg(inplace, "inplace"))


if __name__ == '__main__' :
    unittest.main()