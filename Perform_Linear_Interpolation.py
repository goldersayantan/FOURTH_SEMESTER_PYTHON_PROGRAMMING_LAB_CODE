import scipy.interpolate
import numpy as np
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 7, 13, 21])

interp_func = scipy.interpolate.interp1d(x, y, kind='linear')
print("interpolated value at x = 2.5 :", interp_func(2.5))



