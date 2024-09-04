import sys
import re

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False
print(password)

# Do all the requirement checks here.
if (
    re.search("[a-z]", password)
    and re.search("[A-Z]", password)
    and re.search("[0-9]", password)
    and re.search("[^a-zA-Z0-9]", password) # non-alphanumeric character
    and 6 <= len(password) <= 16
):
    is_valid = True
print(is_valid)
