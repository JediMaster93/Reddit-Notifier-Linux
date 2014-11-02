'''
Created on Oct 29, 2014

@author: jedi
Wrapper for notifications, linux version.
Encapsulated in case i want Windows port

'''
import pynotify, gtk


class Notification(object):
    

    
    def __init__(self, text = "Default text"):
     
        pynotify.init("Reddit Notify")
        self.__text = text
        self.pyNotifiaction = pynotify.Notification(self.__text)
        #self.pyNotifiaction.set_timeout(0)
        #self.pyNotifiaction.set_timeout(pynotify.EXPIRES_DEFAULT)
        self.pyNotifiaction.connect("closed", self.onClosed)
        self.pyNotifiaction.set_timeout(1)
        
        #create a thread that kills notification.
    def onClosed(self, notification):
        gtk.main_quit()
        
    def show(self):
        self.pyNotifiaction.show()
        gtk.main()
    def selfDestruct(self, notification, none):
        print notification
        print "in self destrucst"
        notification.close()
        print "closed notifiaction"
        
        
    def close(self):
        print "close"
        self.pyNotifiaction.close()
    def setText(self, text):
        self.__text = text
        self.pyNotifiaction = pynotify.Notification(self.__text)
        
    def addAction(self, argument, buttonText, method ):
        self.pyNotifiaction.add_action(argument, buttonText, method)
        
    def getPyNotification(self):
        return self.pyNotifiaction
    
    
    
        