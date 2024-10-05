import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server's address and port
server_host = '127.0.0.1'
server_port = 12345

# Connect to the server
client_socket.connect((server_host, server_port))
print(f"Connected to server at {server_host}:{server_port}")

# Get the local and remote address details
print(f"Local address: {client_socket.getsockname()}")
print(f"Remote address (server): {client_socket.getpeername()}")

# Send some data to the server (optional)
message = "Hello, Server!"
client_socket.sendall(message.encode())

# Close the connection
client_socket.close()

