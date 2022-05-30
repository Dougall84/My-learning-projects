#8.4 Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in
#the list and if not append it to the list. When the program completes,
#sort and print the resulting words in alphabetical order.

#fname = input("Enter file name: ")
#fh = open(fname)
fh = open('romeo.txt')
stringy = fh.read()
file = stringy.split()
file.sort()
lst = list()
cnt = 0

for wrds in file:
    
    #print(wrds)
#    print('words',wrds)
#    print('counter',lst[:cntr])
#    print('ounter2',lst[cntr+1:])
#    if wrds == wrds: continue
#    if wrds == lst[counter-2:counter-1]: continue
    lst.append(wrds)

for i in range(len(lst)):
    print(i)
    while cnt < 28:
        print('list i',lst[cnt],lst[cnt+1])
        print(cnt,i)
        if lst[cnt] == lst[cnt+1]:
            rmv = lst[cnt]
            print('remove',rmv)
            lst.remove(rmv)
        cnt = cnt + 1
#    if wrds in lst[counter]:
#        print('remove')
#    print(counter)
#    if lst[counter-1:counter] == lst[counter-2:counter-1]:
#        print('remove')
#        lst.remove(wrds)
    
#lst.sort()

print(lst)
    



