
import requests
import json

url = 'https://gbfs.bcycle.com/bcycle_pacersbikeshare/gbfs.json'
response = requests.get(url)
gbfs = response.json()
print json.dumps(gbfs, indent=4, separators=(',', ': '))
print gbfs['ttl']
for u in gbfs['data']['en']['feeds']:
	#print u['url']
	response = requests.get(u['url']).json()
	print json.dumps(response, indent=4, separators=(',', ': '))