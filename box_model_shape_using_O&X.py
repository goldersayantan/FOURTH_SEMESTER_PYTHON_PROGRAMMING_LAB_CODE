row = int(input("Enter the number of rows: "))
for i in range(1, row + 1):
    for j in range(1, row + 1):
        if i % 2 != 0:
            if j % 2 != 0:
                print("X", end="")
            else:
                print("O", end="")
        else:
            if j % 2 != 0:
                print("O", end="")
            else:
                print("X", end="")
    print("\n")
