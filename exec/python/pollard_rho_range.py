def pollard_rho(n):
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = ((x * x) + 1) % n
        y = ((y * y) + 1) % n
        y = ((y * y) + 1) % n
        d = gcd(abs(x - y), n)
    if d == n:
        return None
    return d

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    factor = pollard_rho(n)
    if factor is None:
        return [n]
    return factorize(factor) + factorize(n // factor)

def is_prime(n):
    if n in [2, 3]:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(lower_bound, upper_bound):
    for i in range(lower_bound, upper_bound + 1):
        if is_prime(i):
            print(i)

find_primes_in_range(1, 100)
