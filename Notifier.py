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
import pickle
import os
class Notifier(object):
    '''
    classdocs
    '''
    seenList = []
    
    def __init__(self):
        self.loadSeenList()
        
    def loadSeenList(self):
        #load from drive
        if os.path.exists("seenList"):
            with open("seenList", "rb") as file:
                self.seenList = pickle.load(file)
        else:
            pass
    def getLatestData(self):
        parser = Parser.Parser(r'http://www.reddit.com/r/gamedeals')
        self.data  = parser.getList()
           
    def handleClick(self,notification, url):
        #opens browser and adds thread to seen list
        webbrowser.open(r'http://www.reddit.com'+url)
        notification.close()
        gtk.main_quit()
        self.seenList.append(url)
        #save list to file
        with open("seenList", "wb") as file:
            pickle.dump(self.seenList, file)
            
        
    def mainLoop(self):
        while True:
            self.getLatestData()
            #dem fancy python list comprehensions.
            #ITS LIKE IM WRITING A NOVEL.
            #anyway it finds a thread that is not in seenlist.
            threadToDisplay = [thread for thread in self.data if thread["permalink"] not in self.seenList]
            
            #get the first thread not in seenlist
            threadToDisplay = threadToDisplay[0]
            #create a notification from thread.
            notification = Notification(threadToDisplay["title"])
            url = threadToDisplay["permalink"]
            
            notification.addAction(url, "Go To Thread", self.handleClick)
            notification.show()
            sleep(3)

            print "Going thru loop"

        
        
                
            