import socket


class client:

    PORT = 5555
    BUFSIZE = 4096

    def sendFile(self,hostip,fileurl):

        ADDR=(hostip,self.PORT)


        bytes=None
        # bytes = open(fileurl).read()

        client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_connection.connect(ADDR)

        with open(fileurl, 'rb') as f:
            bytes = f.read()
        client_connection.sendall(bytes)
        print('file sent')
        client_connection.close()




c=client()
c.sendFile('192.168.43.7','client-image/image3.jpg')

# Procedure to use client api
# from webp2p.client import client
# c=client()

#  c.sendFile(RECEIVER_IP_STRING, IMAGE_URL_STRING)

