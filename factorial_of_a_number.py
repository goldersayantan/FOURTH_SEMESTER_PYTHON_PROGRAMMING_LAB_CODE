num = int(input("Enter a number to calculate factorial: "))
fact = 1
for i in range(num, 0, -1):
    fact = fact * i
print(f"the factorial of {num} is: {fact}")


def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = int(input("Enter a number to calculate factorial: "))
fact = factorial(num)
print(f"the factorial of {num} is: {fact}")
