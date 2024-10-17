import socket

def connect_to_server(host='localhost', port=4481):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Read the welcome message from the server
    response = client_socket.recv(1024).decode('utf-8')
    print("Server Response:", response)
    
    # Send FTP commands to the server
    while True:
        # Get the command from the user
        command = input("Enter FTP command (or QUIT to exit): ").strip()
        
        # Send the command to the server
        client_socket.sendall((command + "\r\n").encode('utf-8'))
        
        # Read the response from the server
        response = client_socket.recv(1024).decode('utf-8')
        print("Server Response:", response)
        
        # If the command was QUIT, break the loop and close the connection
        if command.upper() == 'QUIT':
            break

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    connect_to_server()

