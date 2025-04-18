def prime_numbers(start, stop):
    prime_numbers = []

    for i in range(start, stop + 1):
        if i < 2:
            continue  # Ignore numbers less than 2

        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):  # Check up to sqrt(i)
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(i)

    return prime_numbers


start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))
print("Prime numbers will be:", prime_numbers(start_num, end_num))

#____________

start = int(input("Enter the starting number: "))
stop = int(input("Enter the ending number: "))
for i in range(start, stop + 1):
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
