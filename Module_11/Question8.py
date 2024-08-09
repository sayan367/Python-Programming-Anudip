def fibonacci_series(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b

# Print Fibonacci series up to 50
fibonacci_series(50)
