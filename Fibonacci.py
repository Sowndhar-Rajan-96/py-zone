def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Example usage
num = 10  # Change this value to generate more Fibonacci numbers
print(f"Fibonacci sequence up to {num} terms:", fibonacci(num))
