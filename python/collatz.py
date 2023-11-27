def collatz_sequence(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)  # Include the final 1 in the sequence

# Example: Generate Collatz sequence starting from 6
collatz_sequence(6)

    