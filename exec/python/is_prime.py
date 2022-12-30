def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Bitte gib eine Zahl ein: "))
if is_prime(num):
    print(f"{num} ist eine Primzahl.")
else:
    print(f"{num} ist keine Primzahl.")
