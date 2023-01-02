import pygnfs

# Set the range of numbers to search for prime numbers
start = 1
end = 1000

# Iterate through the range of numbers
for i in range(start, end+1):
  # Use the gnfs function from pygnfs to test for primality
  if pygnfs.gnfs(i):
    # If the number is prime, print it
    print(i)
