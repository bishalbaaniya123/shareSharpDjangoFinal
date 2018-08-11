import socket
from host import Host


class server:

    PORT = 6000
    BUFSIZE = 4096
    PC_name=socket.gethostname()

    def receive(self):
        h=Host()
        host_ip=h.getAllHost().get(self.PC_name)
        print(host_ip)
        if len(host_ip)>0:
            ADDR=(host_ip,self.PORT)
            serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serv.bind(ADDR)
            serv.listen(5)
            print ('listening')

            while True:
                conn,addr=serv.accept()
                print ('client connected...', addr)

                myfile=open('server-image/test.jpg','wb')

                while True:
                    data=conn.recv(self.BUFSIZE)
                    if not data: break
                    myfile.write(data)
                    print ('writing file')

                myfile.close()
                print ('finished writing file')
                conn.close()
                print ('client disconnected')


s=server()
s.receive()