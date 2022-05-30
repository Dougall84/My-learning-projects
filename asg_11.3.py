import re
num_lst = list()


hand = open('regex_sum_1329679.txt')
for line in hand:
    line = line.rstrip()
    search = re.findall('[0-9]+',line)
    num_lst.extend(search)
sum_num = [int(x) for x in num_lst]
print(sum(sum_num))
