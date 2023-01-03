from random import randint

def find_quadratic_congruence(n):
    # Diese Funktion findet eine quadratische Kongruenz x^2 = k (mod n)
    # mit k < n
    k = randint(1, n)
    return k

def tonelli_shanks(n, k):
    # Diese Funktion löst die quadratische Kongruenz x^2 = k (mod n)
    # mithilfe des Tonelli-Shanks-Algorithmus
    # ...

def gcd(a, b):
    # Diese Funktion berechnet den größten gemeinsamen Teiler von a und b
    # mithilfe des euklidischen Algorithmus
    # ...

def gnfs(n):
    # Schritt 1: Finde eine quadratische Kongruenz x^2 = k (mod n)
    # mit k < n
    k = find_quadratic_congruence(n)

    # Schritt 2: Löse die Kongruenz x^2 = k (mod n) mithilfe des
    # Tonelli-Shanks-Algorithmus
    x = tonelli_shanks(n, k)

    # Schritt 3: Berechne ggT(x-y, n) und ggT(x+y, n)
    a = gcd(x-y, n)
    b = gcd(x+y, n)

    # Schritt 4: Falls a und b nicht teilerfremd sind, faktorisiere n
    # als a * b. Andernfalls, wiederhole Schritt 1 mit einem
    # anderen Wert von k.
    if a == 1 or b == 1:
        return gnfs(n)
    else:
        return a, b

def is_prime(n):
    # Diese Funktion verwendet den GNFS, um zu bestimmen, ob n eine Primzahl ist
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        factors = gnfs(n)
        return factors[0] == n and factors[1] == 1

def main():
    # Suche innerhalb der Range von 2 bis 1000 nach Primzahlen
    for i in range(2, 1001):
        if is_prime(i):
            print(i)

if __name__ == "__main__":
    main()
