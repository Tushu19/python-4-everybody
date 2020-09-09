# libraries for XML handling and url data
import xml.etree.ElementTree as ET
import urllib.request

url = input("Enter location: ") # Getting URL from the user
xml = urllib.request.urlopen(url).read() # Opening up the URL
print("Retrieving",url)
print("Retrieved", len(xml), "characters") # To count characters within the URL file
tree = ET.fromstring(xml) # Attaching all the data from the URL to a variable
data = tree.findall('comments/comment') # Going into the right sub-section of the data and attaching that part to a variable
lst = list() # List for calculating sum and count
for data in data: # This for loop is to go through each line that was filtered out from the URL data
    x = int(data.find('count').text) # Diving deeper into the previously filtered data to the parts we want to read
    lst.append(x) # Attaching the found data to a list
# printing out the sum and the count of gathered data using a list
print("Count:", len(lst), "\nSum:", sum(lst))
