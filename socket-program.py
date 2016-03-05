# python 3
# network programming

import socket

# AF_INET | AF_UNIX
# Connection Type : TCP (SOCK_STREAM) , UDP (SOCK_DGRAM)
# protocol
# fd : file descriptor


s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print(s)

server='pythonprogramming.net'


'''
scan port , if port is open connect else return False
'''
def portscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,1024):
    if portscan(x):
        print('Port ',x,'is open')

'''
# connect with server => send request => get results

server_ip=socket.gethostbyname(server)
port=80  # HTTP Port

print(server_ip)

request="GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server,port))
s.send(request.encode()) # convert in proper format
result=s.recv(4096)      # data to be downloaded at a given moment

#print(result)

# Buffer
while(len(result)>0):
    print(result)
    result=s.recv(1024)

'''
