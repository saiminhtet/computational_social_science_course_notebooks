import requests
BASE_URL = "http://api.crossref.org/"

doi = "10.1093/nar/gni170" 
query = "works/"
url = BASE_URL + query + doi
r = requests.get(url)
r.status_code
