import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Bind the socket to the local address and port
local_host = '127.0.0.1.0.0'
local_port = 12345
server_socket.bind((local_host, local_port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Listening on {local_host}:{local_port}")

# Accept a connection
connection, remote_address = server_socket.accept()

print(f"Connected to remote address: {remote_address}")
print(f"Local address: {connection.getsockname()}")
print(f"Remote address: {connection.getpeername()}")

# Close the connection
connection.close()
server_socket.close()

