import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json
lstn = list()
lstc = list()


#re SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open .xml file and read contents
url = input('Enter Url - ')
#url = ('http://py4e-data.dr-chuck.net/comments_1329684.json')
html = urllib.request.urlopen(url, context=ctx).read()
print('Retrieving', url)
print('Retrieved', len(html), 'characters')

info = json.loads(html)

#Add the contents to lists
for item in info['comments']:
    lstn.append(item['name'])
    lstc.append(item['count'])

print('count:',len(lstn))
sum_num = [int(x) for x in lstc]
print('Sum:',sum(lstc))
