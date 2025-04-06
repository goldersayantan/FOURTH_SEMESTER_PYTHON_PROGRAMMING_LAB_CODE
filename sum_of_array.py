limit = int(input("Enter the number of elements you want to keep in the array: "))
my_arr = []
for i in range(limit):
    element = float(input(f"Enter the element no. {i+1}: "))
    my_arr.append(element)

total = 0
for i in my_arr:
    total += i
print(f"The sum of array element is: {total}")
total = sum(my_arr)
print(f"The sum of array elements is: {total}")
