# import the socket library
import socket

# create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
port = 9999

# Bind socket object to the port and Ip address
s.bind(('localhost', port))
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Got connection from', addr, name )

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break