# python 3

'''
server program
open terminal :
$ telnet 172.16.2.56 5555
$ telnet [server IP] [server_port]

Basics:
socket() : AF_INET , SOCK_STREAM(TCP) , host , port
bind()   : ( host , port )
listen() : (queue_size)
accept() : 
send()   : encode data
recv()   : decode data
thread   : client threads
'''

import socket
from _thread import *

host=''
port=5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

s.listen(5)

print('server listening....')

def client_thread(conn):
    conn.send(str.encode('Greetings from client\n'))

    while True:
        data=conn.recv(2048)
        if not data:
            break
        reply=' Server :  ' + data.decode('utf-8')
        conn.sendall(str.encode(reply))
    
    conn.close()
    print('connection closed...\n')
        

while True:
    conn,addr = s.accept()
    print(conn)
    print(addr)
    start_new_thread(client_thread , (conn,))
