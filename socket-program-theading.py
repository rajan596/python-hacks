# python 3

import socket
import threading
from queue import Queue

print_lock=threading.Lock()

target='pythonprogrammming.net'
q=Queue()

def portscan(port):
    s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try:
        conn=s.connect((target,port))
        with print_lock:
            print('port ',port,'is open !')

        conn.close()
         
    except:
        pass
        
def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

# no. of ports to scan=100
for worker in range(1,101):
    q.put(worker)

# no of threads=30
for x in range(30):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()


q.join()    
        
