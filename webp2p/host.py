import nmap
import socket
import json

class Host:

    def getAllHost(self):
        nm=nmap.PortScanner()
        nm.scan(hosts='192.168.43.0/24',arguments='-sn')
        i=0

        hosts={}
        connected_host=nm.all_hosts()
        print (connected_host)
        try:
            for host in connected_host[1:]:

                x, y, z = socket.gethostbyaddr(host)
                hosts[x] = z[0]
                i += 1
        except socket.herror:
            pass
        print(hosts)
        return hosts
