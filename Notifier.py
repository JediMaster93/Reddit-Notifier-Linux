'''
Created on Oct 30, 2014

@author: jedi
'''
#Takes care of when and how nottifications appear

from NotificationLinux import *
import  Parser
import webbrowser
from time import sleep
import gtk
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
           
    def openBroswerUrl(self,notification, url):
        webbrowser.open(url)
        notification.close()
        gtk.main_quit()

        
    def mainLoop(self):
        while True:
            self.getLatestData()
            threadToDisplay = None
            for thread in self.data:
                if thread not in self.seenList:
                    #reddit gives us threads sorted by score
                    #just display the first one that was not seen
                    threadToDisplay = thread
                    break
            notification = Notification(threadToDisplay["title"])
            url = threadToDisplay["url"]
            
            notification.addAction(url, "Go To Thread", self.openBroswerUrl)
            notification.show()
            sleep(3)
            print "Going thru loop"

        
        
                
            