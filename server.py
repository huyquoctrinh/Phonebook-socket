import socket
from utils import *
HOST = '127.0.0.1'  
PORT = 8000        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

while True:
    client, addr = s.accept()
    
    try:
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            str_data = data.decode("utf8")
            if str_data == "quit":
                break
            if not data:
                break
            if str_data == "retrieve_all":
                data = load_data()
                msg = json.dumps(data)
                client.sendall(bytes(msg,encoding="utf-8"))

            msg = input("Server: ")
            client.sendall(bytes(msg, "utf8"))
            
    finally:
        client.close()

s.close()