import socket

# Create a TCP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server running on localhost at port 4481
client_socket.connect(('localhost', 4481))

# Send data to the server
payload = 'Lorem ipsum' * 10000  # Sending large data for testing
client_socket.sendall(payload.encode('utf-8'))

# Receive the server response (if applicable)
data = client_socket.recv(1024)
print("Received from server:", data.decode('utf-8'))

# Close the connection
client_socket.close()

