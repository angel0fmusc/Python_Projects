# Prints the company associated with the given MAC address

import requests, json, sys

# If the user does not enter a MAC address in the command line, exit the script
if len(sys.argv) < 2:
    print("Usage: MAC_Addr_Lookup.py MAC_Address")
    sys.exit()

addr = sys.argv[1]

# payload = {'search': '44:38:39:ff:ef:57'}
# formatted string of URL for request with MAC address
url = f'https://api.macaddress.io/v1?apiKey=at_dgUtmV9XwuiO9hs4JqsU6tzctGMbN&output=json&search={addr}'

response = requests.get(url)

# Check if the request was successful
# Halts the program if not
response.raise_for_status()

# Load JSON response into a Python variable
result = json.loads(response.text)
vendor_details = result['vendorDetails']

print('Requested company name: ' + vendor_details['companyName'])
