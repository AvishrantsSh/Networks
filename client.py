
import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './uds_socket'
print("Connecting to: ", server_address)
try:
    sock.connect(server_address)
except socket.error as msg:
    print(str(msg))
    sys.exit(1)

try:
    message = "Ping"
    print("Sent data: ", message, "\n.")
    sock.sendall(message.encode('utf-8'))

    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print("Received: ", data.decode('utf-8'), "\n.")

finally:
    print("Closing socket")
    sock.close()







    