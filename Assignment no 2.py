#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
# Task no 1
def function1():
    # create 2d array from 1,12 range
    # dimension should be 6row 2 columns
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods
    x = np.arange(1, 12).reshape((6,2))
    return x
"""
expected output:
[[ 1 2]
[ 3 4]
[ 5 6]
[ 7 8]
[ 9 10]
[11 12]]
"""


# In[44]:


# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    x = np.arange(10, 37,dtype=np.float64).reshape((3,3,3))
    return x
"""
 Expected: out put
array([[[10., 11., 12.],
 [13., 14., 15.],
 [16., 17., 18.]],
 [[19., 20., 21.],
 [22., 23., 24.],
 [25., 26., 27.]],
 [[28., 29., 30.],
 [31., 32., 33.],
 [34., 35., 36.]]])
 """


# In[45]:


#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a =np.arange(1, 100*10+1).reshape((100,10))
    x =a[a%5|a%7==0] #wrtie your code here
    return x
"""
 Expected Output:
 [35, 70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,
 490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,
 945, 980]
"""


# In[94]:


#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
    arr = np.arange(9).reshape(3,3)
    temp=arr[:,0].copy()
    arr[:,0]=arr[:,1]
    arr[:,1]=temp
    return arr #wrtie your code here
"""
 Expected Output:
 array([[1, 0, 2],
 [4, 3, 5],
 [7, 6, 8]])
 """


# In[46]:


#task5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
    z =np.zeros((4,5))
    return z
"""
 Expected Output:
 array([[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]])
 """


# In[97]:


#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively

    arr = np.zeros(10) #wrtie your code here
    arr[5]=10
    arr[8]=20 
    return arr


# In[49]:


#task7
def function7():
    # Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
    return np.zeros(4,dtype=np.int64)
"""
 Expected Output:
 array([0, 0, 0, 0], dtype=int64)
 """


# In[50]:


#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    x = np.arange(1, 11).reshape((2,5))
    arr[::]=6 #write your code here
    return x
"""
 Expected Output:
 array([[6, 6, 6, 6, 6],
 [6, 6, 6, 6, 6]], dtype=uint32)
 """


# In[59]:


#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.

    a =np.arange(2,101,2) # write your code here
    return a
    
"""
 Expected Output:
 array([ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26,
 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52,
 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78,
 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100])
 """


# In[75]:


#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from r

    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr-brr.reshape((3,1)) # write your code here

    return subt
"""
 Expected Output:
 array([[2 2 2]
 [2 2 2]
 [2 2 2]])
 """


# In[126]:


#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ans=np.where(arr%2!=0,-1,arr)
    return ans
"""
 Expected Output:
 array([ 0, -1, 2, -1, 4, -1, 6, -1, 8, -1])
 """


# In[143]:


#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below inpu
    # HINT: use stacking concept
    arr = np.array([1,2,3])
    ans = np.hstack((np.repeat(arr,3),arr,arr,arr)) #write your code here
    return ans
"""
 Expected Output:
 array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
 """


# In[12]:


#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans =arr[(arr>5) & (arr<10)]
    return ans
"""
 Expected Output:
 array([6, 9])
 """


# In[32]:


#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between e
    # Hint use split method
    arr = np.arange(10, 34, 1) #write reshape code
    ans = np.split((arr.reshape(8,3)), 4)
    return ans
"""
 Expected Output:
 [array([[10, 11, 12],[13, 14, 15]]),
 array([[16, 17, 18],[19, 20, 21]]),
 array([[22, 23, 24],[25, 26, 27]]),
 array([[28, 29, 30],[31, 32, 33]])]
"""


# In[7]:


#task15
def function15():
    #Sort following NumPy array by the second column
    arr = np.array([[ 8, 2, -2],[-4, 1, 7],[ 6, 3, 9]])
    ans = arr[arr[:,1].argsort()]
    return ans
"""
 Expected Output:
 array([[-4, 1, 7],
 [ 8, 2, -2],
 [ 6, 3, 9]])
 """


# In[1]:


#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans=np.hstack((x, y))
    return ans
"""
 Expected Output:
 [[[1 2]]
 [[2 3]]
 [[3 4]]]
 """
 


# In[163]:


#Task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    return np.where((arr%3==0)&(arr%5==0) , "yes","no")

#Excpected Out
"""
array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
 ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
 ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
 ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
 ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
 ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
 ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
 ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
 ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
 ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],
 dtype='<U3')
"""


# In[35]:


#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = np.count_nonzero(np.in1d(students,piaic)) # Write you code Here
    return x
function18()
 #Expected output: 3


# In[166]:


# Task19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X"
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:
    x=np.arange(1,26).reshape((5,5))
    w=np.transpose(x.copy())
    b=5
    a=(x*w)+b
    return a
    
    #expected output
"""
 array([[ 6, 17, 38, 69, 110],
 [ 17, 54, 101, 158, 225],
 [ 38, 101, 174, 257, 350],
 [ 69, 158, 257, 366, 485],
 [110, 225, 350, 485, 630]])
 """


# In[142]:


#Task20
def fucntion20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def abc(x):
        return x*2+3-2
    return abc(x) #Write your Code here

#Expected Output: array([ 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])


# In[ ]:




