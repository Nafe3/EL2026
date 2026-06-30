import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server(socket, server_address):
    socket.connect(server_address)

def send_data(socket, data):
    socket.sendall(data.encode())

def receive_data(socket):
    return socket.recv(1024).decode()

def close_socket(socket):
    socket.close()

def main():
    socket = create_socket()
    connect_to_server(socket, ("127.0.0.1", 12345))
    send_data(socket, "Hello, server!")
    data = receive_data(socket)
    print(data)
    close_socket(socket)

if __name__ == "__main__":  main()