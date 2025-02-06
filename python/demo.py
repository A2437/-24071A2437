import math

def gcd_lcm(a, b):
    gcd_value = math.gcd(a, b)  # Compute GCD using math module
    lcm_value = (a * b) // gcd_value  # Compute LCM using the formula
    return gcd_value, lcm_value

# Example Usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd_result, lcm_result = gcd_lcm(num1, num2)

print(f"GCD of {num1} and {num2} is: {gcd_result}")
print(f"LCM of {num1} and {num2} is: {lcm_result}")

    
