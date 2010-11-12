# -*- coding:utf-8 -*-
'''
Created on 2010-11-12

@author: leenjewel
'''

from twisted.internet import protocol
from twisted.internet import reactor
from it.gotoandplay.utils.threadevent import ThreadEvent

class SocketClientProtocol(protocol.Protocol):
    def connectionMade(self):
        ThreadEvent.build_event(self.factory, "handleEvent", "onConnection", self)
        return

    def dataReceived(self, data):
        ThreadEvent.build_event(self.factory, "handleEvent", "onDataReceived", data)
        return

class SocketClientFactory(protocol.ClientFactory):
    protocol = SocketClientProtocol
    
    def addEventListener(self, event_obj):
        self.event_obj = event_obj
        return
    
    def handleEvent(self, func_name, *args, **kwargs):
        if self.event_obj:
            ThreadEvent.build_event(self.event_obj, func_name, *args, **kwargs)
        return

def build_connect(event_obj, server_host, server_port):
    socket_client_factory = SocketClientFactory()
    socket_client_factory.addEventListener(event_obj)
    reactor.connectTCP(server_host, server_port, socket_client_factory)
    reactor.run()
    return