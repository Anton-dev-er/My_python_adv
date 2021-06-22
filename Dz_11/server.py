import socket
import time

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(("127.0.0.1", 10002))  # max port 65335
server.listen(5)

conn, addr = server.accept()

with conn, server:
    with open("New_file", "a",  encoding="utf-8") as f:
        while True:
            if data == '':
                break
            data = conn.recv(1024).decode("utf-8")
            f.write(data + "\n")
            time.sleep(1)


