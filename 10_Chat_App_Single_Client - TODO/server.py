import time
import socket
import logging
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (HOST, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!quit'

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s  |  %(name)s  |  %(message)s')
logger.setLevel(10)


def createSocket():
    global server
    try:
        logger.warning("[ESTABLISHING CONNECTION] - Creating Network Socket")
        time.sleep(2)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        logger.info(f"[PORT BINDING] - COMPLETE - {ADDR}")
        time.sleep(1)
        server.listen()
        logger.debug(f"[LISTENING] on port - {PORT}")
        time.sleep(1.5)
    except socket.error as err:
        logger.error(f"[SOCKET CREATION ERROR] - {err}")


def handleClient(conn, addr):
    logger.info(f"[NEW CONNECTION] - {addr} CONNECTED")
    time.sleep(2)
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
    createSocket()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        time.sleep(1)
        logger.info(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")


if __name__ == '__main__':
    logger.debug("[STARTING] Server is Starting")
    start()
