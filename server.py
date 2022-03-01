

import socket
import sys
import os

server_address = './uds_socket'

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print(f"Socket created at {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("Waiting for a connection")
    connection, client_address = sock.accept()
    try:
        print("Incoming request")

        while True:
            data = connection.recv(16)
            if data:
                print("Received data: ", data.decode('utf-8'))
                print("Echoing")
                connection.sendall(data)
            else:
                print("No more data")
                break
            
    finally:
        connection.close()

