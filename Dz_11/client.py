import socket
from datetime import datetime
import time

server = socket.create_connection(("127.0.0.1", 10002))


with open(" source file", encoding="utf-8") as f:
    n = 0
    file = f.read().splitlines()
    with server:
        while n < len(file):
            server.send(f"{datetime.now()}: {file[n]}".encode("utf-8"))

            time.sleep(1)
            n += 1
