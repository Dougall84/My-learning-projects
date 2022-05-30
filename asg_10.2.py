name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hr_counter = dict()
hrs = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):continue
    emails = line.split()
    #print(emails[5])
    hours = emails[5]
    hour = hours.split(':')
    #print(hour[0])
    hrs.append(hour[0])
hrs = sorted(hrs)
#print(hrs)
for hour in hrs:
    hr_counter[hour] = hr_counter.get(hour,0) + 1

for key in hr_counter:
    print(key,hr_counter[key])
