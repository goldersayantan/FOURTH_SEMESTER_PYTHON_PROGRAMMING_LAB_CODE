# wap to find integration
import scipy.integrate
import numpy as np

def func(x):
    return np.sin(x) * np.cos(x)

integral, error = scipy.integrate.quad(func, 0, 1)
print("Integration will be: ", integral)