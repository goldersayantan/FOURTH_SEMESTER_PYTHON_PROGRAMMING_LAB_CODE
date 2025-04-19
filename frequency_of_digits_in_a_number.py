num = int(input("Enter a number: "))
length_of_num = 0
temp = num
while temp > 0:
    length_of_num += 1
    temp = temp // 10
temp = num

count = 0
for i in range(0, 10):
    for j in range(length_of_num):
        rem = temp % 10
        temp = temp // 10
        if i == rem:
            count += 1
    print(f"{i} => {count}")
    count = 0
    temp = num