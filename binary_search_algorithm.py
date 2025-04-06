def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


limit = int(input("Enter the number of elements, you want to keep in the list: "))
my_lst = []
for i in range(limit):
    element = int(input(f"Enter the element number {i + 1}: "))
    my_lst.append(element)
my_lst.sort()
print("The sorted list will be : ", my_lst)
target = int(input("Enter the target element to find: "))
result = binary_search(my_lst, target)
if result != -1:
    print(f"Element found on index : {result}.")
else:
    print("Element not found.")


