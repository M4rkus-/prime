def choose_polynomial(n):
    # Wählen Sie eine Siebgleichung, die für die Faktorisierung von n geeignet ist
    # Beispiel: Wählen Sie ein Polynom 3. Grades
    a = 2
    b = 0
    c = 0
    d = -n
    def polynomial(x):
        return (a * x**3) + (b * x**2) + (c * x) + d
    return polynomial

def sieve(polynomial, n):
    # Implementieren Sie den Sieb-Algorithmus, um Lösungen der Siebgleichung zu finden
    solutions = []
    # Iterieren Sie über alle möglichen Werte von x
    for x in range(2, n):
        # Berechnen Sie den Wert von polynomial für x
        p = polynomial(x)
        # Überprüfen Sie, ob x eine Lösung der Gleichung ist
        if p == 0:
            solutions.append(x)
    return solutions

def find_factorization(solutions, n):
    # Iterieren Sie über alle möglichen Kombinationen von Lösungen
    for i in range(len(solutions)):
        for j in range(i+1, len(solutions)):
            # Überprüfen Sie, ob die Kombination eine Faktorisierung von n ergibt
            if solutions[i] * solutions[j] == n:
                return (solutions[i], solutions[j])
    return "Keine Faktorisierung gefunden."  # Keine Faktorisierung gefunden

def factorize(n):
    polynomial = choose_polynomial(n)
    solutions = sieve(polynomial, n)
    factorization = find_factorization(solutions, n)
    return factorization

# Beispiel für die Verwendung der Funktionen
lower_limit = 2
upper_limit = 100
for n in range(lower_limit, upper_limit):
    factorization = factorize(n)
    if factorization == "Keine Faktorisierung gefunden.":
        print(n)  # n ist eine Primzahl
