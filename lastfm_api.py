import requests
import json

class LastfmApi(object):
	"""docstring for LastfmApi"""
	def __init__(self, api_key, user):
		super(LastfmApi, self).__init__()
		self.api_key = api_key
		self.base_url = "http://ws.audioscrobbler.com/2.0/?"
		self.format = "json"

	def build_url(self):
		return self.base_url + "api_key=" + self.api_key + "&format=" + self.format

	def artist_getTopTags(self, artistmbid):
		base_url = self.build_url()
		final_url = base_url + "&method=artist.getTopTags&mbid=" + artistmbid
		print(final_url)
		#return final_url
		return requests.get(final_url).json()
		