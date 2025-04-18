# WAP TO FIND DETERMINATION OF MATRIX
import numpy as np
import scipy.linalg

A = np.array([[4, 3, 2], [3, 2, 1], [2, 1, 3]])
determination = scipy.linalg.det(A)
print("The determination will be: ", determination)

