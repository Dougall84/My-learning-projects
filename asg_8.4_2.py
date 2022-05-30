#fname = input("Enter file name: ")
#fh = open(fname)
fh = open('romeo.txt')
stringy = fh.read()
file = stringy.split()
lst = list()

for wrds in file:
    #print(wrds)
    if wrds not in lst:
        lst.append(wrds)

lst.sort()
print(lst)
