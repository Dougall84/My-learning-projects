# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
#fname = 'mbox-short.txt'
fh = open(fname)
cnt = 0
ttlnums = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
#    print(line.rstrip())
    srch = line.find(':')
    nums = line[srch+1:]
    nums = float(nums)
    ttlnums = ttlnums + nums 
    cnt += 1
    
#print("Done")
avg = ttlnums / cnt
#print('count',cnt,'numbers',ttlnums,'average',avg)
print('Average spam confidence:',avg)
