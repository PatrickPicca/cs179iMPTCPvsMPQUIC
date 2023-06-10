#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.node import RemoteController
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        switch1 = self.addSwitch('switch1')
        switch2 = self.addSwitch('switch2')

        client = self.addHost('client', ip='10.0.0.1')
        server = self.addHost('server', ip='10.0.4.1')

        self.addLink(client, switch1, cls=TCLink, delay='20ms')
        self.addLink(switch1, switch2, cls=TCLink, delay='20ms', loss=5) #this
        self.addLink(switch2, server, cls=TCLink, delay='20ms') #this
        

topo = CustomTopo()
topos = {'mytopo': CustomTopo}