def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // hcf(a, b)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf_result = hcf(num1, num2)
lcm_result = lcm(num1, num2)

print(f"The HCF of {num1} and {num2} is : {hcf_result}")
print(f"The LCM of {num1} and {num2} is : {lcm_result}")
