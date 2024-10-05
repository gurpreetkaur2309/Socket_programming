import socket

# Create a TCP socket using IPv6
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Bind the socket to the IPv6 address and port
server_socket.bind(('::', 4481))  # '::' means all available IPv6 addresses

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening on IPv6 port 4481...")

# Accept a connection
while True:
    connection, address = server_socket.accept()
    print(f"Connection from {address}")
    connection.close()

