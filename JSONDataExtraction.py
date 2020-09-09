# importing libraries for URL management and for using json
import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ") # Getting user input for URL

dat = urllib.request.urlopen(url) # Opening URL
data = dat.read().decode() # reading and decoding the contents since the info is from an outside sourcefrom the URL
print("Retrieving", url)
print("Retrieved", len(data), "characters")

# sanity check to see if the retrieved data has any syntax errors and might cause an error for json
try:
    js = json.loads(data)
except:
    js = None
    print("json couldn't parse data")

lst = list() # empty list
x = js["comments"] # opening up the dictionary and entering the data of it into a variable
for num in x: # going throgh every value in the dictionary of the previously narrowed down data set
    lst.append(num["count"]) # narrowed down more to the specific data we want and appending it to a list
print("Count:", len(lst),"\nSum:", sum(lst)) # printing out the count and the sum of the gathered data
