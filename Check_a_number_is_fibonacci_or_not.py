num = int(input("Enter a number to check is it fibonacci number: "))
a, b = 0, 1
is_fibonacci = False
while a <= num:
    if a == num:
        is_fibonacci = True
        break
    a, b = b, a+b

if is_fibonacci:
    print(f"{num} is a fibonacci number.")
else:
    print(f"{num} is not a fibonacci number.")

#-------------------------------------------------------

import math

def is_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return math.isqrt(x1)**2 == x1 or math.isqrt(x2)**2 == x2

# Input from user
num = int(input("Enter a number: "))

# Check and print result
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is NOT a Fibonacci number.")
