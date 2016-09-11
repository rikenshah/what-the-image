# http://stackoverflow.com/questions/37012469/duckduckgo-api-getting-search-results
import requests, json, pprint

class duckduckGo(object):
	
	def getInfo(self,nameOfTopic):
		url = "https://api.duckduckgo.com/?q="+nameOfTopic+"&format=json&pretty=1&no_html=1&skip_disambig=1"
		r = requests.get(url)
		# pprint.pprint(r.json()) 
		data = r.json()
		print data['AbstractText']
		return data['AbstractText']