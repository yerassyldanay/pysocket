from socket import *

#
# basic parameters
#

server_name = "localhost"
server_port = 8000

#
# here we will create a client socket
#     SOCK_STREAM - indicates that we are using tcp
#     AF_INET - means underlying network is based on IPv4
#
clientSocket = socket(AF_INET, SOCK_STREAM)

#
# this method accepts an address in the form of tuple
#
clientSocket.connect((server_name, server_port))

#
# here we will send a simple message to the client
#
message_to_send = "hello from client!"
clientSocket.send(bytes(message_to_send))

#
# we will create a buffer of size of 1024 bytes
#
modifiedSentence = clientSocket.recv(1024)
print("Received: ", modifiedSentence)

#
# there is need to close the socket at the end
clientSocket.close()
