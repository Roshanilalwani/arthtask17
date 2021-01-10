import socket
import os
import threading
import time

print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  CHAT  APPLICATION
                           SERVER:2
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("Enter your IP : ")
port =input("Enter your port no : ")

serverip = input("Enter Senders IP : ")

serverport = input("Enter Senders port no : ")


s.bind((ip,int(port)))
def rcvmsg():
    while True:
        x = s.recvfrom(20)
        print("\n Recieved msg : "+x[0].decode())
        time.sleep(1)
def sendmsg():
    while True:
        data = input()
        data = bytes(data, 'utf-8')
        s.sendto(data, (serverip, int(serverport)))
        time.sleep(1)

t1 = threading.Thread(target=rcvmsg)
t2 = threading.Thread(target=sendmsg)

t1.start()
t2.start()
