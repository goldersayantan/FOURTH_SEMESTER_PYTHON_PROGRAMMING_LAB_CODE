def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


rows = int(input("Enter the number of rows: "))
print_pyramid(rows)

# ---------------------------------------------------
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print("")
