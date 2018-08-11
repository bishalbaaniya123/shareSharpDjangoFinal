import socket
from webp2p.host import Host


class server:

    PORT = 5555
    BUFSIZE = 4096
    PC_name=socket.gethostname()

    def receive(self):
        h=Host()
        host_ip=h.getAllHost().get(self.PC_name)
        print(host_ip)
        if len(host_ip)>0:
            ADDR=(host_ip,self.PORT)

            print ('listening')
            i=0;
            serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serv.bind(ADDR)
            serv.listen(5)

            while True:

                conn, addr = serv.accept()
                print('client connected...', addr)
                myfile=open('server-image/1.jpg','wb')
                while True:
                    data=conn.recv(self.BUFSIZE)
                    if not data: break
                    myfile.write(data)
                    print ('writing file')


                myfile.close()
                print ('finished writing file')


                conn.close()
                print ('client disconnected')


# Procedure to use server as api

# from webp2p.server import server
# s=server()
# s.receive(), this directly saves the image to server-image folder inside webp2p folder, you can access it later for displaying