import random

def is_prime(n, k=10):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Find r and d such that n - 1 = 2^r * d with d odd
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k tests
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def find_primes(lower, upper):
    return [n for n in range(lower, upper + 1) if is_prime(n)]

# Test the function
print(find_primes(1, 20))
