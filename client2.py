import socket

# Create a TCP client socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at 'localhost' on port 4481.
client.connect(('127.0.0.1', 4481))

# Print client details.
print(f"Client fileno: {client.fileno()}")
print(f"Client local address: {client.getsockname()}")
print(f"Server remote address: {client.getpeername()}")

# Optionally, send or receive data here (if needed).

# Close the connection.
client.close()

