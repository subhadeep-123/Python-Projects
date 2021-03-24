import socket
import logging
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (HOST, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s  |  %(name)s  |  %(message)s')
logger.setLevel(10)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handleClient(conn, addr):
    logger.info(f"[NEW CONNECTION] - {addr} CONNECTED")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            logger.debug(f"{addr}:  {msg}")
    conn.close()


def start():
    server.listen()
    logger.debug(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        logger.info(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")


if __name__ == '__main__':
    logger.debug("[STARTING] Server is Starting")
    start()
