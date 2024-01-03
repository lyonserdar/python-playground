import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())  # localhost
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 1024  # 1024 bytes
FORMAT = "utf-8"
MSG_DISCONNECT = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if not msg_length:
            continue

        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)

        print(f"[{addr}] {msg}")

        if msg == MSG_DISCONNECT:
            break

        conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()

    print(f"[LISTENING] server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
