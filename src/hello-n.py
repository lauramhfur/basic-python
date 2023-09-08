
# this asks the user for a number and turns the answer
# into an integer
n = int(input("How many times should I loop? "))

# Now, print "Hello, World!" n times.

# For-loop:
for i in range(n):
    print("Hello, World!")

# While-loop - basic:
i = 1
while i < n:
  print("Hello, World!")
  if i == n:
    break
  i += 1