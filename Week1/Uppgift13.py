def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Testa funktionen med ett givet tal
number = 5
result = calculate_factorial(number)
print(f"Fakulteten av {number} är: {result}")
