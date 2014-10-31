'''
Created on Oct 29, 2014

@author: jedi
'''
import urllib2, requests
import json
class Parser(object):
    '''
    classdocs
    Parses data from reddit
    '''


    def __init__(self, url):
        #url that sorts contains data per day.
        self.url = url + r'/top/.json?limit=100&sort=today'
        request = requests.get(self.url)
        self.json =  request.text
        self.json = json.loads(self.json)

    def setUrl(self, url): 
        self.url = url + r'/top/.json?limit=100&sort=today'
        data = urllib2.urlopen(self.url)
        self.json =  data.read()
        self.json = json.loads(self.json)
    def getList(self):
        #parses json into clean list of subreddit data.
        lst = []
        subreddits = self.json["data"]["children"]
        for i in range(25):
            lst.append(subreddits[i]["data"])
        return lst
        
        
