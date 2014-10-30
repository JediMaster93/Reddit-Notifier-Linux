'''
Created on Oct 29, 2014

@author: jedi
'''
#from gi.Repository import Notify

import Notifier, gtk
import pynotify
#action(Notification passed, arugement)
#add_action("arugemnt", "Button text", Method)

def action(n, action):
    print "world"
    print action
if __name__ == '__main__':
    notifier =  Notifier.Notifier()
    notifier.mainLoop()
