fname = input("Enter file name: ")
#fname = 'mbox-short.txt'
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):continue
    words = line.split()
    email = words[1]
    parts = email.split('@')
    count = count + 1
    org = parts[1]
    print(org)

print("There were", count, "lines in the file with From as the first word")
