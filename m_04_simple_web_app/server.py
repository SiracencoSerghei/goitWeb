import socket


def main():
    try:
        host = socket.gethostname()
        port = 5000

        server_socket = socket.socket()
        # server_socket.bind(('', port))
        server_socket.bind((host, port))
        server_socket.listen()

        conn, address = server_socket.accept()
        print(f"Server Connection from: {address}")
        while True:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"Server Received message: {msg}")
            message = input("--> ")
            conn.send(message.encode())
        conn.close()
        server_socket.close()
    except KeyboardInterrupt:
        print("\n\n Server stopped by user")
        

if __name__ == '__main__':
    main()
