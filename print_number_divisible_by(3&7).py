num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
for i in range(num1, num2 + 1):
    if i % 3 == 0 and i % 7 == 0:
        print(i)
