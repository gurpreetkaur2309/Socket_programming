import socket

# Create a TCP/IPv6 socket
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Connect to the server on the same machine (localhost) using IPv6 and port 4481
server_address = ('::1', 4481)  # ::1 is the loopback address for IPv6 (localhost)
client_socket.connect(server_address)

print("Connected to server!")

# Send some data to the server
message = "Hello, IPv6 Server!"
client_socket.sendall(message.encode('utf-8'))

# Close the connection
client_socket.close()

