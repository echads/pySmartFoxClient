# -*- coding:utf-8 -*-
'''
Created on 2010-11-13

@author: leenjewel
'''

from it.gotoandplay.utils.threadevent import ThreadEvent

class SFSEventDispatcher(object):
    def __init__(self):
        self.listeners = {}
    
    def addEventListener(self, event_name, event_obj):
        if not self.listeners.has_key(event_name):
            self.listeners[event_name] = []
        self.listeners[event_name].append(event_obj)
        return
    
    def removeEventListener(self, event_name):
        if self.listeners.has_key(event_name):
            del self.listeners[event_name]
        return
    
    def dispatchEvent(self, event_obj):
        event_name = event_obj.getName()
        if self.listeners.has_key(event_name):
            listeners = self.listeners[event_name]
            for listener in listeners:
                ThreadEvent.build_event(listener, "handleEvent", event_obj)
        return