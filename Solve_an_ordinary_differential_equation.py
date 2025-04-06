from scipy.integrate import solve_ivp

def dydx(t, y):
    return -2 * y

sol = solve_ivp(dydx, [0, 5], [1])
print("Solution at time points: ", sol.t)
print("Values of y: ", sol.y[0])