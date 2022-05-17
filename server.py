import socket
from threading import Thread
import threading
from utils import *
HOST = '127.0.0.1'  
PORT = 8000        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
def run_socket(s):
    json_data = load_data()
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
                    msg = json.dumps(json_data)
                    client.sendall(bytes(msg,encoding="utf-8"))
                # if str_data == "retrieve_one":                
                elif str_data == "retrieve_one":
                    msg = find_someone(json_data,"fullname","Trinh Quoc Huy")
                    # print(msg)
                    msg = json.dumps(msg)
                    client.sendall(bytes(msg,encoding="utf-8"))
                    # client.sendall("end".encode('utf-8'))
        finally:
            client.close()

    s.close()

run_socket(s)

# t = threading.Thread(target = run_socket,args = s)
# t.start()