import scipy.integrate


def func(x):
    return x**2


integral, error = scipy.integrate.quad(func, 0, 1)
print("Integral: ", integral)



