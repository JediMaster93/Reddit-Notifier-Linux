'''
Created on Oct 29, 2014

@author: jedi
'''
#from gi.Repository import Notify

import Notifier
def action():
    print "world"
if __name__ == '__main__':
    notifier =  Notifier.Notifier("derp")
    notifier.mainLoop()