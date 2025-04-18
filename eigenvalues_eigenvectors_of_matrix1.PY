# WAP TO FIND EIGEN VALUES AND EIGEN VECTOR
import numpy as np
import scipy.linalg

A = np.array([[6, 2], [4, 2]])
eigenvalues, eigenvectors = scipy.linalg.eig(A)
print("Eigenvalue will be: ", eigenvalues)
print("Eigenvectors will be: ", eigenvectors)
