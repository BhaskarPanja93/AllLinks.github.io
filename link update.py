from os import system
import socket
from threading import Thread
from time import time, sleep

change_made = 0

def __send_to_connection(connection, data_bytes: bytes):
    connection.sendall(str(len(data_bytes)).zfill(8).encode()+data_bytes)


def __receive_from_connection(connection):
    data_bytes = b''
    length = b''
    for _ in range(12000):
        if len(length) != 8:
            length += connection.recv(8 - len(length))
            sleep(0.01)
        else:
            break
    else:
        return b''
    if len(length) == 8:
        length = int(length)
        for _ in range(12000):
            data_bytes += connection.recv(length - len(data_bytes))
            sleep(0.01)
            if len(data_bytes) == length:
                break
        else:
            return b''
        return data_bytes
    else:
        return b''


def git_push():
    global change_made
    while True:
        sleep(1)
        if change_made:
            if time() - change_made > 3:
                system('git add .')
                system(f'git commit -m "{time()}"')
                system('git push')
                change_made = False


receiver_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_connection.bind(('0.0.0.0', 50010))
receiver_connection.listen()
print('ready')
def receiver():
    global change_made
    connection, address = receiver_connection.accept()
    Thread(target=receiver).start()
    print(address)
    actual_data = eval(__receive_from_connection(connection))
    with open('README.md','w') as file:
        file.write(str(actual_data))
    change_made = time()
Thread(target=receiver).start()
git_push()