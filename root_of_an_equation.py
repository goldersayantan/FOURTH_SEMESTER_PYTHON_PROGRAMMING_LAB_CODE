import scipy.optimize


def equation(x):
    return x**2 - 4  # The roots are x = ±2


# Finding the root with an initial guess of 1
root = scipy.optimize.root(equation, x0=[1])
print("Root is:", root.x[0])  # Extracting the scalar value
