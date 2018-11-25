import socket               # Import socket module
from datetime import datetime
import os

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
print("Sever running...")

while True:

    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)

    current_date = str(datetime.now())
    if os.path.isdir('/opt/users/'):
        dir_present = "Yes"
    else:
        dir_present = "No"


    client_data = c.recv(1024)
    print("Client Data: {}".format(client_data))
    client_data = client_data.decode('utf-8')

    send_data = "Hi, Server has been validated and directory " \
                "present {0} Current Time is: {1}".format(dir_present, current_date)
    send_data = send_data.encode('utf-8') # Encoding from str to bytes

    if client_data == 'validate server':
        c.send(send_data)
    else:
        c.send(b"Thank you for connecting!")

    c.close()                # Close the connection
