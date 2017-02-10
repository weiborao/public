import requests
import json
import sys

if len(sys.argv)<2:
    ip_addr = ''
else:
    ip_addr = sys.argv[1]

resp = requests.get('http://ipinfo.io/' + ip_addr)
json_data = resp.text
prety_data = json.loads(json_data)

print(json.dumps(prety_data, sort_keys=True, indent=4))
sys.exit()

