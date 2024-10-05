import socket

# Create a TCP server socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to address and port (0.0.0.0 listens on all available interfaces).
server.bind(('0.0.0.0', 4481))

# Start listening with a backlog of 128 connections.
server.listen(128)

# Accept a new connection.
connection, addr = server.accept()

# Print details about the connection.
print(f"Connection class: {type(connection)}")
print(f"Server fileno: {server.fileno()}")
print(f"Connection fileno: {connection.fileno()}")
print(f"Local address: {connection.getsockname()}")
print(f"Remote address: {connection.getpeername()}")

