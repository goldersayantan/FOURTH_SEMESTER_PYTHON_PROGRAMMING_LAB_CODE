num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
if num2 > num1:
    for i in range(num2, num1 - 1, -1):
        print(i)
else:
    for i in range(num2, num1 + 1):
        print(i)


