#name = input("Enter file:")
name = 'mbox-short.txt'
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):continue
    email = line.split()
    emails.append(email[1])

counts = dict()


for email in emails:
        counts[email] = counts.get(email,0) + 1
#print(counts)

bigemail = None
bigcount = None
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count
print(bigemail,bigcount)



