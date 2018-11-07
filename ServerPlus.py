#A server that can contain multiple clients

from socket import *
from random import *


def sendAll(message, connection): 
	#go through the list of clients
    for clients in list_of_clients: 
    	#send message to other clients instead of the one who sent the message
        if clients!=connection: 
            try: 
                clients.send(message) 
                print ("Server sent message")
            except: 
                clients.close()

serverPort = 12000

# establish server socket as TCP on IPv4 network
server_socket = socket(AF_INET, SOCK_STREAM)

# binds socket to current host IP with given server port
server_socket.bind(('', serverPort))

# sets server to maintain 10 TCP connections
server_socket.listen(10)

#store Clients here
list_of_clients = []

print ("Server start. .")

while True:
    connection, addr = server_socket.accept()
    #put connection in list
    list_of_clients.append(connection)
  
    # prints the address of the user that just connected 
    print (addr[0] + " connected")
    print (list_of_clients)

    message = connection.recv(1024)

    if message:
    	print ("Server received Message from " + addr[0])
    	sendAll(message,connection)



# closes all socket connections
connection.close()
server_socket.close()