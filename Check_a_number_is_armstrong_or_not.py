num = int(input("Enter a number: "))
temp = num
count = 0

while temp > 0:
    temp = temp // 10
    count += 1

temp = num

new_num = 0

while temp > 0:
    rem = temp % 10
    temp = temp // 10
    new_num += rem ** count

if new_num == num:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")

