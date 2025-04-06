import numpy as np
import scipy.linalg

A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
b = np.array([0, -2, 0])

solution = scipy.linalg.solve(A, b)
print(solution)