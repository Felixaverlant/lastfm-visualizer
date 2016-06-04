#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
from lastfm_api import LastfmApi
import matplotlib.pyplot as plt
import json
import unicodecsv as csv
from io import BytesIO
import time
import codecs

data = pd.read_csv('output-lastfm.log', sep= '	', header=None, names=['date', 'trackname', 'artistname', 'albumname', 'trackmbid', 'artistmbid', 'albummbid'])
df = pd.DataFrame(data)
unique_artist = pd.DataFrame(pd.unique(df['artistmbid'])).dropna()
#print(unique_artist)
last_api = LastfmApi("a280fb8ba1276bc1ab7408dd8c44fe04", "blindcat")


#f = BytesIO()
#writer = csv.writer(f, encoding='utf-8')
#writer.writerow(['artistmbid', 'tag'])

final_data = pd.DataFrame(data=None, columns=['artistmbid', 'tagname'])

#writer = csv.writer(csvfile, delimiter= '\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	
for index, row in unique_artist.iterrows():
	v = last_api.artist_getTopTags(row[0])
	#print(v['toptags']['tag'])
	try:
		for i in v['toptags']['tag']:
			d = pd.DataFrame(data=[[row[0],i['name']]], columns=['artistmbid', "tagname"])
			final_data = final_data.append(d, ignore_index=True)
	except KeyError:
		continue
		#writer.writerow([row[0], i['name']])
	time.sleep(1)

#print(final_data)
final_data.to_csv('tags-final.csv', sep='\t', encoding='utf-8' )