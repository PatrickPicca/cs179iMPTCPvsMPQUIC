from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        client = self.addHost('client')
        server = self.addHost('server')
        
        self.addLink(client,server)

topos = {'mytopo': (lambda: MyTopo())}
