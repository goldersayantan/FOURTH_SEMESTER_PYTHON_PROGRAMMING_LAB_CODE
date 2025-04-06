def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


rows = int(input("Enter the number of rows: "))
print_pyramid(rows)
