p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = int(input("Enter the total number of months: "))
si = (p * r * (t / 12)) / 100
print(f"The simple interest will be: {si}")
