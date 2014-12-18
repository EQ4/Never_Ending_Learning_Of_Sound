import pafy
import os
import sqlite3 as lite
import sys
import datetime

def crawler_database_insert(object_name, duration, keywords, source_url):
	conn = lite.connect('./../db.sqlite3')
	with conn:
		try:
			cur = conn.cursor()
			print "Keywords: " + str(keywords)
			keyword = keywords[0]
			for item in keywords:
				if(item != keyword):
					keyword = keyword + "," + str(item) 

			print "Key: " + str(keyword)
			print "Crawler: INSERTING"
			query = "INSERT INTO neal_main_neal_crawl_model values(NULL, '" + str(object_name) + "', '" + str(duration) + "', '" + str(keyword) + "', '" + str(datetime.datetime.now()) + "', '" + str(source_url) + "');"
			cur.execute(query)
			print "Crawler: INSERTED"
	
		except sqlite3.OperationalError:
			print "Could not insert."


def download(url):
	query_param = url.split('watch?v=')[1]
	v = pafy.new(query_param)
	dur = v.duration
	if(int(dur.split(":")[0]) > 0):
		return
		
	if(int(dur.split(":")[1]) >= 10):
		return
	
	print(v.title)
	print(v.duration)
	print(v.rating)
	print(v.author)
	print(v.length)
	print(v.keywords)
	print(v.thumb)
	print(v.videoid)
	print(v.viewcount)
	print(v.audiostreams)
	
	stream = v.getbestaudio()
	print (stream.url)
	filepath =  os.path.dirname(os.path.abspath(__file__)) + "/static/crawler_downloads/"
	stream.download(filepath = filepath, quiet = True)	
	crawler_database_insert(v.title, v.duration, v.keywords, url)


#download("https://www.youtube.com/watch?v=Yczul_609Gg")

