# http://stackoverflow.com/questions/37012469/duckduckgo-api-getting-search-results
import requests, json, pprint

r = requests.get("https://api.duckduckgo.com/?q=cartoon&format=json&pretty=1&no_html=1&skip_disambig=1")
# pprint.pprint(r.json()) 

data = r.json()

print data['AbstractText']