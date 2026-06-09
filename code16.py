# Code 16: NumPy Basics
# NumPy adds support for large, multi-dimensional arrays and high-level math functions.
# Install: pip install numpy

import numpy as np

print(np.__version__)

# 1D array
arr1 = np.array([1, 2, 3])
print(arr1)

# 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

# 3D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 21, 31], [41, 51, 61], [17, 18, 19]]])
print(arr3)

# Special arrays
print(np.zeros(10))
print(np.zeros((2, 3)))
print(np.zeros(10, dtype=int))
print(np.full((3, 4), 5))
print(np.ones((3, 4)))

# Random arrays
print(np.random.randint(10, size=(3, 4)))
print(np.random.normal(22, 5, (3, 4)))
print(np.random.normal(1, 5, 10))

# 1D random array
x1 = np.random.randint(10, size=6)
print(x1)

# 2D random array
x2 = np.random.randint(10, size=(3, 4))
print(x2)

# 3D random array: 3 matrices, 2 rows, 3 columns
x3 = np.random.randint(10, size=(3, 2, 3))
print(x3)

# Indexing
print(x1[0])
print(x1[2:5])
print(x2[0:2, 0:2])
print(x2[1::, 1:3])

subset = x2[1::, 2::]
print(subset)

print(x2[-1, -1])
print(x3[0, 0, 0])
print(x3[1, 1::, 2::])

# Dimensions and shape
print(x1.ndim)    # 1
print(x2.ndim)    # 2
print(x3.ndim)    # 3

print(x1.shape)
print(x2.shape)
print(x3.shape)

# Another example
X2_a = np.random.randint(10, size=(3, 4))
print(X2_a)
