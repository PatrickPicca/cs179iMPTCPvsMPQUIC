from mininet.topo import Topo
#!/usr/bin/env python
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import OVSKernelSwitch
from mininet.link import TCLink

class MyTopo(Topo):
    def build(self):
        client = self.addHost('client')
        server = self.addHost('server')
        
        switch1 = self.addSwitch('s3')
        switch2 = self.addSwitch('s4')

        self.addLink(client, switch1)
        self.addLink(switch2, server)
        #self.addLink(switch1,switch2, delay='5ms', loss=10)
        #self.cmd (server.cmd('python3 server.py')) 

topos = {'mytopo': (lambda: MyTopo())}
