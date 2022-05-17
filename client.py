import socket
import json
import numpy as np
import cv2
from utils import convert_json_data 

def read_base64(encoded_data):
    nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
    img = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
    cv2.imwrite("./client_img/test.jpg")
    return img
HOST = '127.0.0.1'  
PORT = 8000        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)

try:
    while True:
        msg = input('Client: ')
        s.sendall(bytes(msg, "utf8"))

        if msg == "quit":
            break
        str_recv = ""
        while True:
            data = s.recv(10000000)
            str_recv+= data.decode()
            print(str_recv)
            break
        # data_processed = convert_json_data(str_recv)
        # print(data_processed)
        # print('Server: ', data.decode())
finally:
    s.close()