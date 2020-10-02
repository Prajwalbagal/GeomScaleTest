import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

pos=int(input("enter position"))
rep=int(input("enter times of repetition"))
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
repcount=0
url = input('Enter - ')
for i in range(0,rep):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    repcount+=1
    # Retrieve all of the anchor tags
    tags = soup('a')
    poscount=0
    for tag in tags:
        poscount+=1
        if(poscount==pos and repcount==rep):
            url= tag.get("href",None)
            print(tag.contents[0])
    
""" 
    
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

pos=int(input("enter position"))
rep=int(input("enter times of repetition"))
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tag=soup('a')

for i in range(rep):
    
    urls=tag[pos-1].get("href")
    print(tag[pos-1].text)# Retrieve all of the anchor tags
    htmls = urllib.request.urlopen(urls, context=ctx).read()
    soup = BeautifulSoup(htmls, 'html.parser')
    tag=soup('a')
