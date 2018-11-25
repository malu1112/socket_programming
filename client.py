import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

print("Host {} and Port {}".format(host, port))

s.connect((host, port))
s.send(b"Hello")
print(s.recv(1024))
s.close()               # Close the socket when done
