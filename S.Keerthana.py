# -*- coding: utf-8 -*-
"""Copy of S.Keerthana.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AitFVT-JGq6_i669IbjnYWvY6vGv7iac

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

s="Hi there sam !"
s.split()

# o/p:['Hi', 'there', 'sam', '!']

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742
print('The diameter of {} is {} kilometer '.format (planet,diameter))

# o/p:The diameter of Earth is 12742 kilometer 

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d ['k1'][3]['tricky'][3]['target'][3]

# o/p:'hello'
    
"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

ar = np.zeros(10)
ar

# o/p:array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

ar1 = np.ones(10)*5
ar1

#o/p:array([5., 5., 5., 5., 5., 5., 5., 5., 5., 5.])


"""## 5. Create an array of all the even integers from 20 to 35"""

a = np.arange(20,36,2)
a
# o/p:array([20, 22, 24, 26, 28, 30, 32, 34])

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

l1=[[0,1,2],[3,4,5],[6,7,8]]
arr = np.array(l1)
arr
"""
o/p:array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
"""
"""## 7. Concatinate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

a = np.array([1,2,3])
b = np.array([4,5,6])
output=np.concatenate((a,b),axis=0)
print(output)

# o/p:[1 2 3 4 5 6]

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

k1={"shapes":["circle","square","triangle"],"size":[2,4,6]}
df = pd.DataFrame(k1)
print(df)
"""
o/p:
     shapes  size
0    circle     2
1    square     4
2  triangle     6
"""
"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

dates = pd.date_range(start= '1-1-2023',end='2-10-2023')
# also can do with for val in dates: #print(val)
print(dates)
"""
o/p:DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
               '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
               '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12',
               '2023-01-13', '2023-01-14', '2023-01-15', '2023-01-16',
               '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20',
               '2023-01-21', '2023-01-22', '2023-01-23', '2023-01-24',
               '2023-01-25', '2023-01-26', '2023-01-27', '2023-01-28',
               '2023-01-29', '2023-01-30', '2023-01-31', '2023-02-01',
               '2023-02-02', '2023-02-03', '2023-02-04', '2023-02-05',
               '2023-02-06', '2023-02-07', '2023-02-08', '2023-02-09',
               '2023-02-10'],
              dtype='datetime64[ns]', freq='D')
 """
"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

df = pd.DataFrame(lists,columns=['numbers','names','age'])
print(df)
"""
o/p:   numbers names  age
0        1   aaa   22
1        2   bbb   25
2        3   ccc   24
"""
