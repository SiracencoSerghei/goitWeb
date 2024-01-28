import socket


def main():
    try:
        host = socket.gethostname()
        port = 5000

        client_socket = socket.socket()
        client_socket.connect((host, port))
        print(f'Client was connected with: {host}')
        message = input("--> ")
        while message.lower().strip() != 'exit':
            client_socket.send(message.encode())
            msg = client_socket.recv(1024).decode()
            print(f"Client Received message: {msg}")
            message = input("--> ")

        client_socket.close()
    except KeyboardInterrupt:
        print("\n\n Client stopped by user")


if __name__ == '__main__':
    main()
