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

        switch1 = self.addSwitch('switch1', listenPort=6634)  # Set the OpenFlow port for switch1
        switch2 = self.addSwitch('switch2', listenPort=6634)

        self.addLink(client, switch1)
        self.addLink(switch2, server)
        self.addLink(switch1, switch2, cls=TCLink, loss=5)

def create_topology():
    topo = MyTopo()
    controller = RemoteController('c0', ip='10.0.0.10', port=6653)  # Specify the Ryu controller
    net = Mininet(topo=topo, controller=controller)
    net.start()

    # Add the command to set the switch flow
    net.get('switch1').cmd('ovs-ofctl add-flow switch1 action=normal')
    net.get('switch2').cmd('ovs-ofctl add-flow switch2 action=normal')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
