import requests
import json
q_id = input()
url = f"https://hacker-news.firebaseio.com/v0/item/{q_id}.json"
response=requests.get(url)
#print(response.headers)
dic=response.json()
print(dic['title'])
'''
import os
os.system()'''
