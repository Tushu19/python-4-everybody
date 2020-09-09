import numpy as np

## Creating Arrays
myList = [1,2,3,]
## converting list to arrays
x = np.array(myList)
print(x)

print('1----')
y = np.array([4,5,6])
print(y)

print('2----')
## making multi dimensional arrays
m = np.array([[7,8,9],[10,11,12]])
## to get the shape of the array
print(m.shape)

print('3----')
## to return evenly spaced values with an interval
n = np.arange(0,30,2)
print(n)

print('4----')
## to reshape an array
n = n.reshape(3,5)
print(n)

print('5----')
## similar to arange, except we tell it how many intervals we want between 2 numbers and it returns the numbers evenly
o = np.linspace(0, 4, 9)
print(o)

print('6----')
## to change the dimensions in place
o.resize(3,3)
print(o)

print('7----')
##  np.ones returns an array of ones
print(np.ones((3,2)))

print('9----')
## np.zero reutnrs an array of zeros
print(np.zeros((2,3)))

print('10----')
## np.eye reutnrs a square shaped array with the diagonal values being 1 and the rest of the values being zeros
print(np.eye((3)))

print('11----')
## np.diag prints the values from an array into a new square shapped array, diagonally with the rest of the numbers being zeros
print(np.diag(y))

print('12----')
## repeats the array with the order of the numbers in place
print(np.array([1,2,3,4] * 3))

print('13----')
## repeats each number in the array#
print(np.repeat([1,2,3,4], 3))

print('14----')
p = np.ones([2,3], int)
print(p)

print('15----')
## vstack stacks arrays on top of each other, the 2*p just means the array on top is multipled by 2
print(np.vstack([p,2*p]))

print('16----')
## hstack is the same as vstack except it stacks horizontally
print(np.hstack([p,2*p]))

print('----------------------------------------------')
## OPERATIONS
print(x + y)
## performs element wise addition between 2 arrays
print('17----')
## performs element wise mltiplication between 2 arrays
print(x * y)
print('18----')
## ## squares each element in an array
print(x**2)
print('19----')
## returns the dot product of of 2 arrays
print(x.dot(y))
print('20----')
## making 2 arras on top of one another and squaring the elements in the first array to get the elements in the second array
z = np.array([y,y**2])
print(z)
print('21----')
## ## returns the shape of an array
print(z.shape)
## transpose the shape of an array, basically swap the values of the orginal shape of an array
print(z.T)
## get the shape of a transposed array
print(z.T.shape)
print('22----')
## returns the data type of elements in an array
print(z.dtype)
print('23----')
## changes the data type (in this case to a float) of an array
z=z.astype('f')
print(z.dtype)
print('----------------------------------------------')

## Math functions
a = np.array([-4,-2,1,3,5])
## from this array it returns the sum, the maximum value, the minimum value, the mean of an array and the standard deviation of an array, respectively
print(a.sum(), a.max(), a.min(), a.mean(), a.std())
print('24----')
## to get the index of the maximum or minimum value in an array
print(a.argmax(), a.argmin())

## Indexing and sliing
print('----------------------------------------------')
## creating an array with the squares of 0 to 12
s = np.arange(13)**2
print(s)
print('25----')
## to get the first index of an array, to get the 5th index of an array and to get the values from the first value and up to (but not including) the 4th value
print(s[0], s[4], s[0:3])
print('----')
## getting the values from the second value and up to but not including the 6th value
print(s[1:5])
print('----')
## getting the values starting from the 4th value from the end of the array
print(s[-4:])
print('----')
## getting the values starting from the 5th from the end and up to but not including the second value from the end of the array
print(s[-5:-2])
print('----')
## making an array of values from 0 and up to, but not including, 36 and reshaping the array to fit into a 6x6 array
r = np.arange(36).reshape((6,6))
print(r)
print('----')
## to get the value in the second row and the second column (remember the first row and column are both 0)
## it is row and column in that order
print(r[2,2])
print('----')
## to get the elements from the 3rd column and up to, but not including, the 6th column in the 3rd row
print(r[3,3:6])
print('----')
## to get the elements from the first 5 columns in the first 2 rows
print(r[:2,:6])
print('----')
## to get every seond element from the last row
print(r[-1,::2])
print('----')
## to get the elements from an array that are over a specific amount
print(r[r>30])
print('----')
## to determine which elements are over a certain number
print([r>30])
print('----')
## to set the maximum limit of an array to a certain value
r[r>30] = 30
print(r)
print('----')
## creates an array which is a slice of an already existing array. In this case, r2 is the first 3 columns and rows of array r
r2 = r[:3,:3]
print(r2)
print('----')
## sets all the elements of an array to a specific value
r2[:] = 0
print(r2)
print('----')
## if we look at the original array r, the elements in the first 3 rows and colums are set to the latest values of r2(which was originaly a slice of the first 3 rows and columns of the array r)
print(r)
print('----')
## creates a copy of an array without changing the previously copied array
r_copy = r.copy()
print(r_copy)
print('----')
## change all the elements in r_copy to 10
r_copy[:] = 10
## you can see by changing the copy of an array it does not change the elements in the original array
print(r_copy,'\n\n', r)
print('----------------------------------------------')

## Iterating over arrays
## creating an array that has random integers, that has 9 values and is in a (4,3) shape
test = np.random.randint(0,10, (4,3))
print(test)
print('----')
## iterate by row of an array
for row in test:
    print(row)
print('----')
## iterates by row index
for i in range(len(test)):
    print(test[i])
print('----')
## combine the previous 2 ways of iterating by using enumerate
for i, row in enumerate(test):
    print('row', i, 'is', row)
print('----')
## squares the value of each element in array test
test2 = test**2
print(test2)
print('----')
## iterating by rows while combining 2 arrays
for i,j in zip(test,test2):
    print(i , '+', j, '=', i+j)
print('----')
x = np.arange(36)
y = x.reshape((6,6))
print(y)
print(y[2:4,2:4])
