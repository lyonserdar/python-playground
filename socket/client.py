import socket

SERVER = socket.gethostbyname(socket.gethostname())  # localhost
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 1024  # 1024 bytes
FORMAT = "utf-8"
MSG_DISCONNECT = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    server_msg = client.recv(2048).decode(FORMAT)
    print(server_msg)


send("Hello, World!")
send(MSG_DISCONNECT)
