# import libraries for URL management, json and SSL certificate checks
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Enter location: ") # Asking for user input

parms = dict() # Creating a dictionary
parms['address'] = address # API key managing
if api_key is not False:
     parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms) # This adds the address (which is converted to where it can function as a URL) to the serviceurl

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx) # Opens the URL (serviceurl + encoded address)
data = uh.read().decode() # Decodes the data (because it came in from outside and could be in a different language) and allows us to read it
print('Retrieved', len(data), 'characters')

try: # Sanity check to make sure there aren't any syntax errors in the received data and json and load it up for us into a variable
    js = json.loads(data)
except:
    js = None

# Finds the information we need by going down the information tree and printing it
print("Place id", js["results"][0]["place_id"])
