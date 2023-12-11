def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

# Örnek kullanım:
n = 10
fibonacci_sequence = fibonacci(n)
print(f"Fibonacci {n} sayısı: {fibonacci_sequence}")
