# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WeHjnkcHNiLow1mLtSX0a6fx28-HfAq3

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

s.split()

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

print('The diameter of {} is {} kilometer '.format (planet,diameter))

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d ['k1'][3]['tricky'][3]['target'][3]

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

a1 = np.zeros(10)
a1

a2 = np.ones(10)*5
a2

"""## 5. Create an array of all the even integers from 20 to 35"""

a3 = np.arange(20,36,2)
a3

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

li=[[0,1,2],[3,4,5],[6,7,8]]
a4 = np.array(li)
a4

"""## 7. Concatinate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

a = np.array([1,2,3])
b = np.array([4,5,6])
result=np.concatenate((a,b),axis=0)
print(result)

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

k1={"fruits":["apple","mango","watermelon"],"count":[5,9,10]}
df = pd.DataFrame(k1)
print(df)

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

dates = pd.date_range(start= '1-1-2023',end='2-10-2023')
print(dates)

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

df = pd.DataFrame(lists,columns=['numbers','names','age'])
print(df)