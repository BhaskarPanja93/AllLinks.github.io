from os import system
import socket
from threading import Thread
from time import time, sleep

BUFFER_SIZE = 1024*100
change_made = False


def __send_to_connection(connection, data_bytes: bytes):
    data_byte_length = len(data_bytes)
    connection.send(f'{data_byte_length}'.zfill(8).encode())
    connection.send(data_bytes)


def __receive_from_connection(connection):
    length = b''
    while len(length) != 8:
        length+=connection.recv(8-len(length))
    length = int(length)
    data_bytes = b''
    while len(data_bytes) != length:
        data_bytes += connection.recv(length-len(data_bytes))
    return data_bytes


def git_push():
    global change_made
    while True:
        if change_made:
            if time() - change_made > 3:
                system('git add .')
                system('git commit -m ".."')
                system('git push https://github.com/BhaskarPanja93/AllLinks.github.io')
                change_made = False
            else:
                sleep(1)
        else:
            sleep(1)



receiver_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_connection.bind(('0.0.0.0', 50010))
receiver_connection.listen()
print('ready')
def receiver():
    global change_made
    connection, address = receiver_connection.accept()
    Thread(target=receiver).start()
    print(address)
    data = eval(__receive_from_connection(connection))
    key, value = list(data.keys())[0], list(data.values())[0]
    with open('README.md','r') as file:
        actual_data = eval(file.read())
    actual_data[key] = value
    with open('README.md','w') as file:
        file.write(str(actual_data))
    change_made = time()
Thread(target=receiver).start()
git_push()
