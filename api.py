import requests
import json

url = 'https://ajax.googleapis.com/ajax/services/feed/load?v=1.0&q=http://www.digg.com/rss/index.xml&num=10'

result = requests.get(url)

json_result = result.json()
to_txt = ''

to_txt = "Feed Url : "+ json_result['responseData']['feed']['feedUrl']+"\n"
to_txt += "Feed Title : "+ json_result['responseData']['feed']['title']+"\n"
to_txt += "Feed Description : "+ json_result['responseData']['feed']['description']+"\n\n"



for result_value in json_result['responseData']['feed']['entries']:
	to_txt += '{} : {}\n'.format("Title", result_value['title'])
	to_txt += '{} : {}\n'.format("Content", result_value['content'])
	to_txt += '{} : {}\n'.format("Link", result_value['link'])
	to_txt += '{} : {}\n\n'.format("Data Published", result_value['publishedDate'])


with open('digg_feed.txt', 'w') as outputfile:
	outputfile.write(to_txt)