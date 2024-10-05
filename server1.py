import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a public host and a port
server_socket.bind(('localhost', 12345))

# Become a server and listen for connections
server_socket.listen(1)
print("Server is listening...")

# Accept a connection from a client
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Send a response to the client
client_socket.send(b'Hello from the server!')

# Close the connection
client_socket.close()

