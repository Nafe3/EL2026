import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
server.bind((ip, 12345))
server.listen(5)
print("Server is running on", ip)
while True:
    client, addr = server.accept()
    print("Connected by", addr)
    while True:
        data = client.recv(1024)
        if not data:
            print("No data received")
            client.send("no data received".encode('utf-8'))
            break
        print("Received data:", data.decode("utf-8"))
        client.send(b'200 OK')