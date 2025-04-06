rows = int(input("Enter the number of rows: "))
print("The left side pyramid will be: ")
for i in range(1, rows + 1):
    for j in range(0, i):
        print("*", end="")
    print("")
