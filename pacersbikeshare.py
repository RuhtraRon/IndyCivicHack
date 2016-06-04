
import requests

url = 'https://gbfs.bcycle.com/bcycle_pacersbikeshare/gbfs.json'
response = requests.get(url)
print response.json()
