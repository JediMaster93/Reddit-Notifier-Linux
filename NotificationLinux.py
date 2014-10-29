'''
Created on Oct 29, 2014

@author: jedi
Wrapper for notifications
'''
import pynotify
class Notification(object):
    

    
    def __init__(self, text = "Default text"):
        pynotify.init("App name")
        self.__text = text
        self.pyNotifiaction = pynotify.Notification(self.__text)
        
    def show(self):
        self.pyNotifiaction.show()
        
    def setText(self, text):
        self.__text = text
        self.pyNotifiaction = pynotify.Notification(self.__text)
        
        
        
        
        