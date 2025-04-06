import numpy as np
import scipy.linalg

A = np.array([[3, 2], [1, 4]])
b = np.array([5, 6])

x = scipy.linalg.solve(A, b)
print("Solution: ", x)
