import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

#re SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open .xml file and read contents
#url = input('Enter Url - ')
url = ('http://py4e-data.dr-chuck.net/comments_42.json')
html = urllib.request.urlopen(url, context=ctx).read()


info = json.loads(url)
print('User count:', len(info))

#for item in info:
#    print('Name', item['name'])
#    print('Id', item['id'])
#    print('Attribute', item['x'])
