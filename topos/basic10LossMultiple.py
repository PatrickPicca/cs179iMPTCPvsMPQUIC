#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.node import RemoteController
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        client = self.addHost('client', ip='10.0.0.1', defaultRoute=None)
        server = self.addHost('server', ip='10.0.4.1', defaultRoute=None)

        switch1 = self.addSwitch('switch1', ip='10.0.1.1')  
        switch2 = self.addSwitch('switch2', ip='10.0.2.1')
        switch3 = self.addSwitch('switch3', ip='10.0.3.1')

        self.addLink(client, switch1, cls=TCLink, delay='10ms')
        self.addLink(client, switch2, cls=TCLink, delay='10ms')
        self.addLink(switch1, switch3, cls=TCLink, delay='100ms',bw=10)
        self.addLink(switch2, switch3, cls=TCLink, delay='50ms',bw=10, loss=10)
        self.addLink(switch3, server, cls=TCLink, delay='10ms')
        

topo = CustomTopo()
topos = {'mytopo': CustomTopo}