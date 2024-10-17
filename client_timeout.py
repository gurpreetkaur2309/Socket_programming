import socket

# Server ka IP aur port jahan par connection establish karna hai
server_address = ('127.0.0.1', 4481)

# TCP socket create karte hain
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        # Server ke saath connect karna
        client_socket.connect(server_address)

        # Server ko data send karna
        message = "Hello, Server!"
        client_socket.sendall(message.encode())

        # Server se data receive karna (yahan hum 4096 bytes tak read karenge)
        data = client_socket.recv(4096)
        print(f"Received from server: {data.decode()}")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Socket ko close karna
        client_socket.close()

