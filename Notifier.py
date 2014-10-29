'''
Created on Oct 30, 2014

@author: jedi
'''
#Takes care of when and how nottifications appear

from NotificationLinux import *
import  Parser

class Notifier(object):
    '''
    classdocs
    '''
    seenList = []
    
    def __init__(self):
        self.loadSeenList()
        
    def loadSeenList(self):
        #load from drive
        pass
    def getLatestData(self):
           parser = Parser.Parser(r'http://www.reddit.com/r/gamedeals')
           self.data  = parser.getList()
           
        
    def mainLoop(self):
        self.getLatestData()
        threadToDisplay = None
        for thread in self.data:
            if thread not in self.seenList:
                #reddit gives us threads sorted by score
                #just display the first one that was not seen
                threadToDisplay = thread
                break
        notification = Notification(thread["title"])
        notification.show()
        
                
            