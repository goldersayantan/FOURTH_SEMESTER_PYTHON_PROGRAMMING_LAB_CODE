limit = int(input("Enter the number of elements you want to keep in the array: "))
my_arr = []
for i in range(limit):
    element = float(input(f"Enter the element no. {i+1}: "))
    my_arr.append(element)
smallest_element = my_arr[0]
for i in range(len(my_arr)):
    if smallest_element > my_arr[i]:
        smallest_element = my_arr[i]
print(f"The smallest element in the array is: {smallest_element}")

largest_element = my_arr[0]
for j in range(len(my_arr)):
    if largest_element < my_arr[j]:
        largest_element = my_arr[j]
print(f"The largest element in the array is: {largest_element}")
