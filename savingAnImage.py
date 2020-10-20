

import requests

'''
this code saves an image from a website using the request library and saves the image on your desktop
'''

myRequest = requests.get("https://imgs.xkcd.com/comics/python.png")

with open("/Users/ironman/Desktop/comic.png", 'wb')as file:
    file.write(myRequest.content)



