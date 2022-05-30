fname = input("Enter file name: ")
fh = open(fname)

# print the file, and make it uppercase
for line in fh:
    line = line.rstrip().upper()
    print(line)
