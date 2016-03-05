import socket
import sys

'''
open terminal
$ telnet localhost 5555
'''

host=''
port=5555

s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

# s.listen(queued_connections)
s.listen(5)

conn ,addr =s.accept()

print(conn)
print(addr)


    
