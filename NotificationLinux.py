'''
Created on Oct 29, 2014

@author: jedi
Wrapper for notifications, linux version.
Encapsulated in case i want Windows port

'''
import pynotify, gtk,webbrowser
class Notification(object):
    

    
    def __init__(self, text = "Default text"):
        pynotify.init("App name")
        self.__text = text
        self.pyNotifiaction = pynotify.Notification(self.__text)
        
    def show(self):
        self.pyNotifiaction.show()
        gtk.main()
        
    def close1(self):
        print "close"
        self.pyNotifiaction.close()
    def setText(self, text):
        self.__text = text
        self.pyNotifiaction = pynotify.Notification(self.__text)
        
    def addAction(self, argument, buttonText, method ):
        self.pyNotifiaction.add_action(argument, buttonText, method)
        
    def getPyNotification(self):
        return self.pyNotifiaction
        