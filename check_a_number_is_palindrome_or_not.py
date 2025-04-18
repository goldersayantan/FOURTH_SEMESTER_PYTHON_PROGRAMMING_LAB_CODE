num = int(input("Enter a number to check if it is palindrome or not:  "))
total = 0
temp = num
while temp > 0:
    rem = temp % 10
    total = rem + (total * 10)
    temp = temp // 10

if total == num:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")


#______________________________________________
num = int(input("Enter a number: "))
temp = num
new_num = 0
count = 0
while temp > 0:
    count += 1
    temp = temp // 10

temp = num
while temp > 0:
    rem = temp % 10
    new_num += rem * (10 ** (count - 1))
    count -= 1
    temp = temp // 10

if new_num == num:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

