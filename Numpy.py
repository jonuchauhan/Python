import numpy as np

# one dimensional array
a = np.array([1, 2, 3, 4])
print(a)
# two dimensional array
b = np.array([[2, 3, 4, 5, 6, 7], [10, 9, 8, 7, 6, 4]])
print(b)

# get the dimension of array
print(a.ndim)
print(b.ndim)
# get shape
print(a.shape)  # 4 values only on one axis
print(b.shape)

# get type
print(a.dtype)

# get size

print(a.itemsize)

print(a.size)  # total size or total number of elements

print(b.size)

# accesssing and changing the specific element

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

print(a)

# get a specific element
"first value is row number starting value is 0 and second value is column number starts with zero"
print(a[0, 3])
# get a specific row
print(a[0])
# get a specific column
": means all rows "
print(a[:, 2])

"[startindex:endindex:stepsize]"
print(a[0, 1:7:3])

# change values
a[1, 2] = 15
print(a)

a[:, 2] = 15  # all rows and second column
print(a)

a[:, 1] = [20, 21]
print(a)

c = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]])
print(c)
"https://www.youtube.com/watch?v=QUT1VHiLmmI&ab_channel=freeCodeCamp.org     22:23"
print(c[:0:])