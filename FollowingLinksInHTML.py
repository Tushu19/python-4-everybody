# import for online html data
import urllib.request, urllib.parse, urllib.error
# import for handling html data
from bs4 import BeautifulSoup
# SSL certificate errors (better safe than sorry sanity checks)
import ssl
import re
# ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# getting first url, position and count numbers
url = input('Enter URL:')
position = int(input("Enter position:"))-1
count = int(input("Enter count:"))
# opening first url and sorting html lines (that meet our requirements) into a variable
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print("Retrieving:", url)
# this loop takes the approriate link from the files, opens them, and opens the next appropriate link within the next file
for i in range(count):
    x = None
    #getting url from html line
    link = tags[position].get('href', None)
    # finds the name in the link string
    x = re.findall('[A-Z][a-z]+',link)
    print("Retrieving:",link)
    #opens the next corresponding link and starts the process over again
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
# prints the last remaining contents of x after the for loop in a non list format
print(*x)
