# Wap to find differntiation
from scipy.integrate import solve_ivp

def dydx(x, y):
    return -10 * y

sol = solve_ivp(dydx, [0, 5], [1])
print("Solution at time points:", sol.t) 
print("Values of y:", sol.y[0]) 

