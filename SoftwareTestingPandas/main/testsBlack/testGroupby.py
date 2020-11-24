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
This file contains multiple black box tests for the function groupby from the library Pandas. 

A groupby operation involves some combination of splitting the object, applying a function, and combining the results. 
This can be used to group large amounts of data and compute operations on these groups.
'''
class TestPandasGroupby(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    def testSurvived(self):
        data = self.df.groupby(['Survived']).size()
        self.assertEqual(data[0],545)
        self.assertEqual(data[1],342)
        self.assertEqual(data.dtypes, 'int64')
        """
        Survived
        0    545
        1    342
        dtype: int64
        """

    def testSex(self):
        data = self.df.groupby(['Sex']).size()
        self.assertEqual(data[0],314)
        self.assertEqual(data[1],573)
        self.assertEqual(data.dtypes, 'int64')
        """
        Sex
        female    314
        male      573
        dtype: int64
        """

    def testSurvivedSex(self):
        data = self.df.groupby(['Survived','Sex']).size()
        self.assertEqual(data[0,'female'], 81)
        self.assertEqual(data[0,'male'], 464)
        self.assertEqual(data[1,'female'], 233)
        self.assertEqual(data[1,'male'], 109)
        self.assertEqual(data.dtypes, 'int64')
        """
        Survived  Sex   
        0         female     81
                  male      464
        1         female    233
                  male      109
        dtype: int64
        """

    def testBySurvivedSex(self):
        data = self.df.groupby(by=['Survived','Sex']).size()
        self.assertEqual(data[0,'female'], 81)
        self.assertEqual(data[0,'male'], 464)
        self.assertEqual(data[1,'female'], 233)
        self.assertEqual(data[1,'male'], 109)
        self.assertEqual(data.dtypes, 'int64')
        """
        Survived  Sex   
        0         female     81
                  male      464
        1         female    233
                  male      109
        dtype: int64
        """
    
    def test_as_index(self):
        data = self.df.groupby(by='Age', as_index=True).size()
        self.assertEqual(len(data.index), 89)
        self.assertEqual(data[0.42], 1)
        data = self.df.groupby(by='Age', as_index=False).size()
        self.assertEqual(len(data.index), 89)
        self.assertEqual(data.iloc[0]['Age'], 0.42)
        """
        as_index=True
        .....Age
        0.42     1
        0.67     1
        0.75     2
        0.83     2
        0.92     1
                ..
        as_index=False
            Age  size
        0    0.42     1
        1    0.67     1
        2    0.75     2
        3    0.83     2
        4    0.92     1
        ..    ...   ...
        """
    
    def testGroupingOnCollumns(self):
        data = self.df.groupby('Survived')['Sex'].size()
        self.assertEqual(data[0],545)
        self.assertEqual(data[1],342)
        """
        ....Survived
        0    545
        1    342
        Name: Sex, dtype: int64
        """

    def test_sort(self):
        data = self.df.groupby('Age',sort=True).size()
        self.assertEqual(len(data.index), 89)
        self.assertEqual(data[0.42], 1)
        self.assertEqual(data.iloc[0], 1)
        data = self.df.groupby('Age',sort=False).size()
        self.assertEqual(len(data.index), 89)
        self.assertEqual(data[0.42], 1)
        self.assertEqual(data.iloc[0], 39)
        """
        sort=True
        ......Age
        0.42     1
        0.67     1
        0.75     2
        0.83     2
        0.92     1
                ..
        sort=False
        Age
        22.00    39
        38.00    12
        26.00    21
        35.00    21
        27.00    26
                ..
        """

    def test_axis(self):
        dataIndex = self.df.groupby(by=['Name','Survived','Sex'],axis='index').size()
        data0 = self.df.groupby(by=['Name','Survived','Sex'],axis=0).size()
        self.assertTrue(dataIndex.equals(data0))
        dataColumns = self.df.groupby(by=['Name','Survived','Sex'],axis='columns').size()
        data1 = self.df.groupby(by=['Name','Survived','Sex'],axis=1).size()
        self.assertTrue(dataColumns.equals(data1))

    def test_level(self):
        data = self.df.groupby('Age').size()

if __name__ == '__main__' :
    unittest.main()
