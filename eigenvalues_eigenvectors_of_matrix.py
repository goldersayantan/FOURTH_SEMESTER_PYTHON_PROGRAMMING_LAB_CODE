import numpy as np
import scipy.linalg

A = np.array([[4, -2], [1, 1]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = scipy.linalg.eig(A)

# Print real values (if applicable)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
