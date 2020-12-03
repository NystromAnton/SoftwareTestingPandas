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
This file contains multiple black box tests for the function groupby from the library Pandas. 

A groupby operation involves some combination of splitting the object, applying a function, and combining the results. 
This can be used to group large amounts of data and compute operations on these groups.
'''
class TestPandasGroupby(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv ('../src/data/titanic.csv')

    def testGroupingOnCollumns(self):
        """
        Ex.
        ....Survived
        0    545
        1    342
        Name: Sex, dtype: int64
        """

        data = self.df.groupby('Survived')['Sex'].size()
        self.assertEqual(data[0],545)
        self.assertEqual(data[1],342)

    def test_by(self):
        """
        Used to determine the groups for the groupby. If a dict or Series is passed, 
        the Series or dict VALUES will be used to determine the groups. 
        If an ndarray is passed, the values are used as-is determine the groups. 
        A label or list of labels may be passed to group by the columns in self. 
       
        Ex.
        Sex
        female    314
        male      573
        dtype: int64

        Survived
        0    545
        1    342
        dtype: int64

        Survived  Sex   
        0         female     81
                  male      464
        1         female    233
                  male      109
        dtype: int64
        """

        data = self.df.groupby(['Sex']).size()
        self.assertEqual(data[0],314)
        self.assertEqual(data[1],573)
        self.assertEqual(data.dtypes, 'int64')

        data = self.df.groupby(['Survived']).size()
        self.assertEqual(data[0],545)
        self.assertEqual(data[1],342)
        self.assertEqual(data.dtypes, 'int64')


        data = self.df.groupby(by=['Survived','Sex']).size()
        self.assertEqual(data[0,'female'], 81)
        self.assertEqual(data[0,'male'], 464)
        self.assertEqual(data[1,'female'], 233)
        self.assertEqual(data[1,'male'], 109)
        self.assertEqual(data.dtypes, 'int64')


        data = self.df.groupby(['Survived','Sex']).size()
        self.assertEqual(data[0,'female'], 81)
        self.assertEqual(data[0,'male'], 464)
        self.assertEqual(data[1,'female'], 233)
        self.assertEqual(data[1,'male'], 109)
        self.assertEqual(data.dtypes, 'int64')


    def test_axis(self):
        """
        Split along rows (0) or columns (1).
        """
        dataIndex = self.df.groupby(by=['Name','Survived','Sex'],axis='index').size()
        data0 = self.df.groupby(by=['Name','Survived','Sex'],axis=0).size()
        self.assertTrue(dataIndex.equals(data0))
        dataColumns = self.df.groupby(by=['Name','Survived','Sex'],axis='columns').size()
        data1 = self.df.groupby(by=['Name','Survived','Sex'],axis=1).size()
        self.assertTrue(dataColumns.equals(data1))


    def test_level(self):
        """
        If the axis is a MultiIndex (hierarchical), group by a particular level or levels.

        Does not have an affect on the titanic dataset because it is not hierarchical.
        """
        data = self.df.groupby(level=0).size()
        data = self.df.groupby(by=['Survived','Sex'], level=0).size()

    
    def test_as_index(self):
        """
        For aggregated output, return object with group labels as the index. 
        Only relevant for DataFrame input. as_index=False is effectively “SQL-style” grouped output.

        In the titanic dataset:
        False, grouping by Age does not set it as index for the new dataset.
        True, grouping by Age sets it as index for the new dataset
        Ex.
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
        data = self.df.groupby(by='Age', as_index=True).size()
        self.assertEqual(len(data.index), 89)
        self.assertEqual(data[0.42], 1)
        data = self.df.groupby(by='Age', as_index=False).size()
        self.assertEqual(len(data.index), 89)
        self.assertEqual(data.iloc[0]['Age'], 0.42)
    

    def test_sort(self):
        """
        Sort group keys in the Titanic dataset. 
        False, do not sort the groupby dataset.
        True, sort the groupby dataset by index.

        Ex.
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
        data = self.df.groupby('Age',sort=True).size()
        self.assertEqual(len(data.index), 89)
        self.assertEqual(data[0.42], 1)
        self.assertEqual(data.iloc[0], 1)
        data = self.df.groupby('Age',sort=False).size()
        self.assertEqual(len(data.index), 89)
        self.assertEqual(data[0.42], 1)
        self.assertEqual(data.iloc[0], 39)


    def test_group_keys(self):
        """
        When calling apply, add group keys to index to identify pieces. 
        """
        dataTrue = self.df.groupby(by=['Pclass'], level=0, group_keys=True).size()
        dataFalse = self.df.groupby(by=['Pclass'], level=0, group_keys=False).size()
        self.assertTrue(dataTrue.equals(dataFalse))

        dataTrue = self.df.groupby(by=['Survived','Sex','Pclass'], level=0, group_keys=True).size()
        dataFalse = self.df.groupby(by=['Survived','Sex','Pclass'], level=0, group_keys=False).size()
        self.assertTrue(dataTrue.equals(dataFalse))

    def test_squeeze(self):
        """
        Reduce the dimensionality of the return type if possible, otherwise return a consistent type.
        Deprecated since version 1.1.0.
        """
        dataTrue = self.df.groupby(by=['Survived','Sex','Pclass'], squeeze=True).size()
        dataFalse = self.df.groupby(by=['Survived','Sex','Pclass'], squeeze=False).size()
        self.assertTrue(dataTrue.equals(dataFalse))
    
    def test_observed(self):
        """
        This only applies if any of the groupers are Categoricals.  
        If True:  onlyshow observed values for categorical groupers.  
        If False:  show all valuesfor categorical groupers.

        This is only applied to catagorical datasets. Applying observed True/False to 
        the Titanic dataset does nothing.
        """
        dataTrue = self.df.groupby(by=['Survived','Sex','Pclass'], observed=True).size()
        dataFalse = self.df.groupby(by=['Survived','Sex','Pclass'], observed=False).size()
        self.assertTrue(dataTrue.equals(dataFalse))

    def test_dropna(self):
        """
        If  True,  and  if  group  keys  contain  NA  values,  NA  values  
        together  withrow/column will be dropped.  If False, NA values will 
        also be treated asthe key in groups.

        The original dataset contains no NA values so dropna True/False so 
        it returns the same dataset.
        Three rows in the column 'Name' was replaced with NA values. 
        Returns two different datasets with different lengths. 
        """
        dfNA = self.df
        dataTrue = dfNA.groupby(by=['Name'], dropna=True).sum()
        dataFalse = dfNA.groupby(by=['Name'], dropna=False).sum()
        self.assertTrue(dataTrue.equals(dataFalse))
        self.assertEqual(len(dataTrue.index),887)
        self.assertEqual(len(dataFalse.index),887)

        dfNA.loc[0, 'Name'] = np.nan
        dfNA.loc[1, 'Name'] = np.nan
        dfNA.loc[2, 'Name'] = np.nan
        dataTrue = dfNA.groupby(by=['Name'], dropna=True).sum()
        dataFalse = dfNA.groupby(by=['Name'], dropna=False).sum()
        self.assertFalse(dataTrue.equals(dataFalse))
        self.assertEqual(len(dataTrue.index),884)
        self.assertEqual(len(dataFalse.index),885)

    def testNoArgument(self):
        """
        Testing groupby with no arguments. 
        Returns a TypeError to indicate a bad function call.
        """
        with self.assertRaises(TypeError):
            data = self.df.groupby()            

    def testInvalidArgument(self):  
        """
        Testing groupby with invalid arguments.
        Returns a NameError to indicate that a argument is wrong.
        """
        with self.assertRaises(NameError):
            data = self.df.groupby(argument)
        
    def testColumnNotFound(self):
        """
        Testing groupby with columns that does not exist in the dataset.
        Returns KeyError to indicate that the columns was not found.
        """
        with self.assertRaises(KeyError):
            data = self.df.groupby("")
        
        with self.assertRaises(KeyError):
            data = self.df.groupby("nonexistingcolumn")

if __name__ == '__main__' :
    unittest.main()