import socket


class client:

    PORT = 9876
    BUFSIZE = 4096

    def sendFile(self,hostip,fileurl):

        ADDR=(hostip,self.PORT)


        bytes=None
        # bytes = open(fileurl).read()
        with open(fileurl, 'rb') as f:
            bytes = f.read()
        client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_connection.connect(ADDR)

        client_connection.send(bytes)
        client_connection.close()




c=client()
c.sendFile('192.168.1.4','client-image/DSC_1437.jpg')

