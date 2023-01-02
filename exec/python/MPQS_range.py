import pympqs

# Set the range of numbers to search for prime numbers
start = 1
end = 1000

# Iterate through the range of numbers
for i in range(start, end+1):
  # Use the mpqs function from pympqs to test for primality
  if pympqs.mpqs(i):
    # If the number is prime, print it
    print(i)
