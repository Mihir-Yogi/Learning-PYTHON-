import numpy as np

# Numpy arrays

# 1D array
arr1 = np.array([5,6,7,9])
print(arr1)
print(f"{arr1.ndim}D")
print("=" * 50)

# 2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(f"{arr2.ndim}D")
print("=" * 50)

# 3D array
arr3 = np.array([
    [
        [1,2,3],[4,5,6],[7,8,9]
    ],
    [
        [1,2,3],[4,5,6],[7,8,9]
    ]
])
print(arr3)
print(f"{arr3.ndim}D")

