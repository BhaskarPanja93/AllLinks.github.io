from os import system
import socket
from threading import Thread

BUFFER_SIZE = 1024*100


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

receiver_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_connection.bind(('0.0.0.0', 50010))
receiver_connection.listen()
print('ready')
def receiver():
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
    system('git add .')
    system('git commit -m ".."')
    system('git push')
Thread(target=receiver).start()