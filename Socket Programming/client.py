# Import socket module
import socket

# create a client object
c = socket.socket()
print("Socket successfully created")

# connect to the server on local computer
c.connect(('127.0.0.1', 9999))

# Send data
name = input("Enter name")
c.send(name.encode())

# receive data from the server and decoding to get the string.
print(c.recv(1024).decode())

# close the connection
c.close()