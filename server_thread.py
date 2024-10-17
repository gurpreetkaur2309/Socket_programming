import socket
import threading

class Connection:
    CRLF = "\r\n"

    def __init__(self, client_socket):
        self.client = client_socket

    def gets(self):
        return self.client.recv(1024).decode('utf-8').strip()

    def respond(self, message):
        self.client.sendall((message + self.CRLF).encode('utf-8'))

    def close(self):
        self.client.close()

class CommandHandler:
    def __init__(self, connection):
        self.connection = connection

    def handle(self, request):
        cmd = request[:4].strip().upper()
        if cmd == "USER":
            return "230 Logged in anonymously"
        elif cmd == "SYST":
            return "215 UNIX Type: L8"
        elif cmd == "QUIT":
            return "221 Goodbye"
        else:
            return "502 Command not implemented"

class ThreadPerConnectionServer:
    def __init__(self, port=21):
        self.control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.control_socket.bind(('', port))
        self.control_socket.listen(5)
        print(f"FTP Server running on port {port}")
    
    def run(self):
        threading.excepthook = lambda args: print(f"Exception in thread: {args.exc_type}, {args.exc_value}")
        while True:
            client_socket, client_address = self.control_socket.accept()
            print(f"Accepted connection from {client_address}")
            connection = Connection(client_socket)
            
            thread = threading.Thread(target=self.handle_client, args=(connection,))
            thread.start()

    def handle_client(self, connection):
        connection.respond("220 OHAI")
        handler = CommandHandler(connection)
        
        while True:
            request = connection.gets()
            if request:
                response = handler.handle(request)
                connection.respond(response)
            else:
                connection.close()
                break

if __name__ == "__main__":
    server = ThreadPerConnectionServer(port=4481)
    server.run()

