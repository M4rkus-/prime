import random

# Diese Funktion führt den Miller-Rabin-Test aus
def is_probably_prime(n, k=5):
  if n < 2:
    return False
  if n == 2 or n == 3:
    return True

  # Wir nehmen an, dass n keine Primzahl ist, und versuchen, diese Annahme zu widerlegen
  is_prime = False

  # Berechne (n - 1) / 2
  s = 0
  r = n - 1
  while r & 1 == 0:
    s += 1
    r //= 2

  # Führe k Tests durch
  for _ in range(k):
    a = random.randrange(2, n - 1)
    x = pow(a, r, n)
    if x != 1 and x != n - 1:
      j = 1
      while j < s and x != n - 1:
        x = pow(x, 2, n)
        if x == 1:
          return False
        j += 1
      if x != n - 1:
        return False

  # Wenn alle Tests bestanden wurden, nehmen wir an, dass n wahrscheinlich eine Primzahl ist
  return True

# Teste einige große Zahlen auf Primzahl-Eigenschaft
numbers_to_test = [1234567890123456789, 98765432109876543219876, 100000000000000000000000000000001]
for n in numbers_to_test:
  if is_probably_prime(n):
    print(f"{n} ist wahrscheinlich eine Primzahl")
  else:
    print(f"{n} ist wahrscheinlich keine Primzahl")
