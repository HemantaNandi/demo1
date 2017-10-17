#!/usr/bin/python
#
# Screen scraper based API for BookMyShow.


from __future__ import print_function
#from future.standard_library import install_aliases
#install_aliases()

#from urllib.parse import urlparse, urlencode
#from urllib.request import urlopen, Request
#from urllib.error import HTTPError

import json
import os

#from flask import Flask
#from flask import request
#from flask import make_response
import re
from urllib.request import urlopen
# Flask app should start in global layout
#app = Flask(__name__)
city ='Durgapur'

#@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
    city ='Durgapur' # parameters.get("geo-city")
    
class BookMyShowClient(object):
  NOW_SHOWING_REGEX = '{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"Filter Impression:category\\\/now showing"},"products":\[{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}\]}}}'
  COMING_SOON_REGEX = '{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"category\\\/coming soon"},"products":{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}}}}'

  def __init__(self, location = city):
    self.__location = location.lower()
    self.__url = "https://in.bookmyshow.com/%s/movies" % self.__location
    self.__html = None

  def __download(self):
   # req = urllib.Request(self.__url, headers={'User-Agent' : "Magic Browser"})
   # html = urllib.urlopen(req).read()
    html = urlopen(self.__url).read().decode('utf-8')
    return html

  def get_now_showing(self):
    if not self.__html:
      self.__html = self.__download()
    now_showing = re.findall(self.NOW_SHOWING_REGEX, self.__html)
    return now_showing

  def get_coming_soon(self):
    if not self.__html:
      self.__html = self.__download()
    coming_soon = re.findall(self.COMING_SOON_REGEX, self.__html)
    return coming_soon

if __name__ == '__main__':
  # Test code.
  bms_client = BookMyShowClient(city)
  now_showing = bms_client.get_now_showing()
  #print str(now_showing), ' movies playing in Durgapur .'
for xs in now_showing:
   print(" ".join(map(str, xs)))
  #return {
       # "speech": now_showing,
       # "displayText": now_showing,
        # "data": data,
        # "contextOut": [],
       # "source": "apiai-weather-webhook-sample"
   # }
    
