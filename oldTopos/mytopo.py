#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.node import RemoteController
from mininet.cli import CLI

class MyTopo(Topo):
    def build(self):
        client = self.addHost('client')
        server = self.addHost('server')
        
        self.addLink(client,server)

def create_topology():
    topo = MyTopo()
    controller = RemoteController('c0', ip='10.0.0.10', port=6653)  # Specify the Ryu controller
    net = Mininet(topo=topo, controller=controller)
    #net.addNAT().configDefault()
    #net.start()
    #CLI(net)
    #net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
