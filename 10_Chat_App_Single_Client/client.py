import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


# Helper Function
def main():
    sending = True
    while sending:
        msg = input()
        if msg == 'q':
            sending = False
        send(msg)


if __name__ == '__main__':
    main()
