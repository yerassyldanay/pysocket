from socket import *

#
# indicate the port number using which socket accepts messages
#
server_port = 8000

#
# AF_INET - indicates that network layer is based on IPv4
# SOCK_STREAM - indicates that we are using tcp
#
serverSocket = socket(AF_INET, SOCK_STREAM)

#
# starting a server
#
serverSocket.bind(("", server_port))
serverSocket.listen()

while True:
    #
    # letting client tcp to communicated with this server
    # created a buffer of size - 1024 bytes
    #
    clientSocketConn, addr = serverSocket.accept()
    sentence = clientSocketConn.recv(1024)

    #
    # creatign a message and sending it over tcp
    #
    message_to_send = "Got: " + sentence + " | Message from server "
    clientSocketConn.send(message_to_send)

    clientSocketConn.close()