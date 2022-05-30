import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
nums = int()
lst = list()

#re SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open .xml file and read contents
url = input('Enter Url - ')
#url = ('http://py4e-data.dr-chuck.net/comments_1329683.xml')
html = urllib.request.urlopen(url, context=ctx).read()

# Use ElemenrTree to access data in .xml format
tree = ET.fromstring(html)
counts = tree.findall('.//count')

for count in counts:
    nums = count.text
    lst.append(nums)

#convert items in list to integers
sum_num = [int(x) for x in lst]

print('Retriving: ', url)
print('Items counted: ', len(lst))
print('Sum: ', sum(sum_num))
