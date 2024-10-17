import socket

# Create a TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 4481))
server_socket.listen(5)
server_socket.setblocking(False)  # Non-blocking mode

while True:
    try:
        # Accept connections in non-blocking mode
        connection, address = server_socket.accept()
        print(f"Connection from {address}")
        
        # Handle the connection (e.g., read data, send response)
        data = connection.recv(1024)  # Example of receiving data
        if data:
            print("Received:", data.decode())
        
        # Close the connection
        connection.close()
    
    except BlockingIOError:
        # Do other important work here while no connection is available
        continue

