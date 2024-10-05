

# Python Socket Programming

This repository contains Python scripts demonstrating basic socket programming using IPv4 and IPv6. The scripts implement simple client-server communication. The server must be started first, and then the client connects to the server to send and receive messages.

## Repository Structure

```
├── server.py
├── client.py
├── README.md
```

### Files

- `server.py`: Python script to start the server. The server listens for incoming client connections and processes data.
- `client.py`: Python script to run the client, which connects to the server, sends data, and receives responses.

## Getting Started

### Prerequisites

To run these scripts, you need:

- Python 3.x installed on your machine
- Basic understanding of socket programming

### Running the Code

To run the server and client scripts, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gurpreetkaur2309/Socket_programming.git
   cd Socket_programming
   ```

2. **Run the Server**:
   Open a terminal and run the following command to start the server:

   ```bash
   python server.py
   ```

   The server will start listening on the specified IP address and port (as defined in the script).

3. **Run the Client**:
   In a new terminal, run the client script:

   ```bash
   python client.py
   ```

   The client will connect to the server and send/receive messages.

## How It Works

1. **Server**: 
   - The server listens for connections on a specified IP and port.
   - Once a client connects, it can receive and send data.
   
2. **Client**: 
   - The client connects to the server using its IP and port.
   - After establishing the connection, the client sends data and receives responses.

## Notes

- Make sure to run the server before running the client, otherwise the client will not be able to connect.
- If both the server and client are running on the same machine, the client connects to `localhost` (or `127.0.0.1` for IPv4, and `::1` for IPv6).
- You can modify the port and IP address in the scripts as needed.

## License

This project is licensed under the MIT License.

---

