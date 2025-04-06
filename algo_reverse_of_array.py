limit = int(input("Enter the number of elements you want to keep in the array: "))
my_arr = []
for i in range(limit):
    element = float(input(f"Enter the element no. {i+1}: "))
    my_arr.append(element)
print(f"The original list is: {my_arr}")
reverse_array = []
for i in range(len(my_arr) - 1, -1, -1):
    reverse_array.append(my_arr[i])
print(f"The reverse array will be: {reverse_array}")

# ----------------------------------------------------------------

limit = int(input("Enter the number of elements in the array: "))
my_lst = []
for i in range(limit):
    element = input(f"Enter the element number {i + 1} : ")
    my_lst.append(element)
print("The original list is: ", my_lst)
print("The reverse list will be: ", my_lst[::-1])    
