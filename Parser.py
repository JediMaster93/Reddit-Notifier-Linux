'''
Created on Oct 29, 2014

@author: jedi
'''
import urllib2, requests
import json
from time import sleep
class Parser(object):
    '''
    classdocs
    Parses data from reddit
    '''


    def __init__(self, url):
        #url that sorts contains data per day.
        self.url = url + r'/top/.json?limit=100&sort=today'
        
        resultCode = 0
        while resultCode != 200:
            request = requests.get(self.url)
            resultCode = request.status_code
            print resultCode
            sleep(1)
            
        
        self.json =  request.text
        self.json = json.loads(self.json)

    def setUrl(self, url): 
        self.url = url + r'/top/.json?limit=100&sort=today'
        data = urllib2.urlopen(self.url)
        self.json =  data.read()
        self.json = json.loads(self.json)
    def getList(self):
        #parses json into clean list of thread data.
        # end list contains threads with things like url, permalink, title, ect.
        lst = []
        threads = self.json["data"]["children"]
        
        lst = [thread["data"] for thread in threads]
        return lst
        
        
