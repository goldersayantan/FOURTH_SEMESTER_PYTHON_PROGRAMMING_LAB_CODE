num = int(input("Enter a number to check is it fibonacci number: "))
a, b = 0, 1
is_fibonacci = False
while a <= num:
    if a == num:
        is_fibonacci = True
        break
    a, b = b, a+b

if is_fibonacci:
    print(f"{num} is a fibonacci number.")
else:
    print(f"{num} is not a fibonacci number.")

