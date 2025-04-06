# decimal = int(input("Enter a number: "))
# binary = ""
# num = decimal
# while num > 0:
#     remainder = num % 2
#     binary = str (remainder) + binary
#     num = num // 2
# print(f"Binary number equivalent to {decimal} is: {binary}")


def decimal_to_binary(num):
    if num == 0:
        return "0"

    binary = ""
    temp = num
    while temp > 0:
        rem = temp % 2
        temp = temp // 2
        binary = str(rem) + binary  # Append at the beginning

    print(f"The binary equivalent of decimal number {num} is: {binary}")


num = int(input("Enter a decimal number: "))
decimal_to_binary(num)
