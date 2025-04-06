def fibonacci_in_range(start, end):
    fib_series = []
    a, b = 0, 1

    while a <= end:
        if a >= start:
            fib_series.append(a)
        a, b = b, a + b

    return fib_series


start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))
print(fibonacci_in_range(start_range, end_range))


def fibonacci_series(limit):
    a = 0
    b = 1
    count = 0
    my_lst = []
    while count <= limit:
        my_lst.append(a)
        a, b = b, a + b
        count += 1
    return my_lst


limit = int(input("Enter the limit of numbers: "))
print("The fibonacci series will be: ", fibonacci_series(limit))
