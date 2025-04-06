import scipy.optimize


def f(x):
    return x**2 + 2*x + 1  # This simplifies to (x+1)^2, which has a minimum at x = -1


# Minimizing the function, initial guess should be an array
result = scipy.optimize.minimize(f, x0=[0])
print("Minimum occurs at x =", result.x[0])  # Extracting the scalar value

