import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3] # extraction of the 2nd and 3rd elements of sys.argv, which corresponds to the command and the string, respectively.

match command: # determining whether to encode or decode based on command
    case "encode":
        # Implement the encoding here
        encoding = []
        for i in x:
            encoding.append(hex(ord(i)))
        print("".join(encoding))

    case "decode":
        # Implement the decoding here
        x = x.split('0x')
        decoding = []
        for i in x[1:]:
            decoding.append(chr(int(i, 16)))
        print("".join(decoding))