from os import system
import socket
from threading import Thread
from time import time, sleep

BUFFER_SIZE = 1024*100
change_made = False


def __send_to_connection(connection, data_bytes: bytes):
    data_byte_length = len(data_bytes)
    connection.send(str(data_byte_length).encode())
    if connection.recv(1) == b'-':
        connection.send(data_bytes)
    if connection.recv(1) == b'-':
        return


def __receive_from_connection(connection):
    length = int(connection.recv(BUFFER_SIZE))
    connection.send(b'-')
    data_bytes = b''
    while len(data_bytes) != length:
        data_bytes += connection.recv(BUFFER_SIZE)
    connection.send(b'-')
    return data_bytes

def git_push():
    global change_made
    while True:
        if change_made:
            if time() - change_made > 3:
                system('git add .')
                system('git commit -m ".."')
                system('git push')
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