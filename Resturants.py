from math import *
import random
import json
import urllib3
import requests
import pprint

'''
This code will generate information using an API request
'''

myRequest = requests.get("https://api.dailysmarty.com/posts")
myRequest.json()
pprint.pprint(myRequest.json()['posts'][0])
pprint.pprint(myRequest.json()['posts'][0]['url_for_post'])


