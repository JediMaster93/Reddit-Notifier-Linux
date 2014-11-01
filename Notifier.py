'''
Created on Oct 30, 2014

@author: jedi
'''
#Takes care of when and how nottifications appear

import gtk
from time import sleep
import webbrowser

from NotificationLinux import *
import  Parser
import gobject


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
           
    def handleClick(self,notification, url):
        webbrowser.open(r'http://www.reddit.com'+url)
        notification.close()
        gtk.main_quit()
        self.seenList.append(url)
        
    def mainLoop(self):
        while True:
            self.getLatestData()
            threadToDisplay = None
            for thread in self.data:
                if thread["permalink"] not in self.seenList:
                    #reddit gives us threads sorted by score
                    #just display the first one that was not seen
                    threadToDisplay = thread
                    break
            notification = Notification(threadToDisplay["title"])
            url = threadToDisplay["permalink"]
            
            notification.addAction(url, "Go To Thread", self.handleClick)
            notification.show()
            sleep(3)
            print "Going thru loop"

        
        
                
            