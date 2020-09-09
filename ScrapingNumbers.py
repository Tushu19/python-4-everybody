#import re - to use re.findall function
import re
#to access data from a URL
import urllib.request, urllib.parse, urllib.error
#to clean up the messy HTML lines to use in algorithms
from bs4 import BeautifulSoup
#for all the SSL certificate errors, use this all the time when working with data online
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# get url of file
url = input('Enter - ')
#clean up all the HTML lines so it can be used in algorithms
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#the previous 2 sets of algorithms are important and act like opening a local file
#variables for final result
sum = 0
count = 0
#variable to hold all the HTML lines
tags = soup('span')
#this for loop is to convert all the HTML lines to a string first
for tag in tags:
    x = str(tag)
    #to extract all the numbers in each HTML line that got converted to a string
    y = re.findall('[0-9]+', x)
    #this for loop is to convert all the strings of integers to ints to perform calculations using them
    for num in y:
        #converting string of numbers, that were found in the strings that were converted to a string from being an HTML line, into an int
        num = int(num)
        sum += num
        count = count + 1
#printing results
print("Count", count)
print("Sum", sum)
