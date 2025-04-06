def left_side_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print("")


rows = int(input("Enter the number of rows, you needed: "))
print("The pyramid will be: ")
left_side_pyramid(rows)
