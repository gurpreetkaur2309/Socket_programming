import socket
import select

# Server IP aur port
host = '127.0.0.1'
port = 4481
timeout = 5  # seconds
max_attempts = 3  # Kitni baar timeout ke baad retry kare

# TCP socket create karte hain
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}...")

    attempts = 0  # Timeout attempts ko track karne ke liye

    while attempts < max_attempts:
        # Connection accept karne ke liye timeout implement karte hain
        ready_to_read, _, _ = select.select([server_socket], [], [], timeout)

        if ready_to_read:
            client_socket, client_address = server_socket.accept()
            print(f"Connected to {client_address}")

            # Data receive karte hain with timeout condition
            ready = select.select([client_socket], [], [], timeout)

            if ready[0]:
                try:
                    # Data ko read karna
                    data = client_socket.recv(4096)
                    if data:
                        print(f"Received from {client_address}: {data.decode()}")
                        client_socket.sendall(b"Data received!")
                    else:
                        print(f"Connection closed by {client_address}")
                except socket.error as e:
                    print(f"Socket error: {e}")
            else:
                print(f"Timeout: No data received from {client_address} in {timeout} seconds.")

            # Client socket ko close kar dena
            client_socket.close()
        else:
            attempts += 1  # Timeout ke baad attempts increment karna
            print(f"No client connected in {timeout} seconds. Attempt {attempts} of {max_attempts}")

    print("Maximum attempts reached, server shutting down.")

