import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Send data to the server
client_socket.send(b'Hello from the client!')

# Receive response from the server
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Close the connection
client_socket.close()

