def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []
    if n <= 0:
        return fibonacci_sequence
    elif n == 1:
        fibonacci_sequence.append(0)
        return fibonacci_sequence
    elif n == 2:
        fibonacci_sequence.extend([0, 1])
        return fibonacci_sequence
    else:
        a, b = 0, 1
        fibonacci_sequence.extend([a, b])
        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)
            a, b = b, c
        return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence up to", num_terms, "terms:", fibonacci_sequence)

      

