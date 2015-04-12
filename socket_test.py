import socket
import threading
import datetime
from threading import Timer


def student(teacher_address):

    HOST=''
    PORT=12341

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.bind( (HOST, PORT))

    while True:

    	a=input('Are You Confused??? Press y')

    	if a=='y':

    		s.sendto(a.encode(),teacher_address)
    
def teacher():

    HOST=''
    PORT=12343

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.bind( (HOST, PORT) )
    s.settimeout(1)

    while True:
        

        endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)

        x=0

        #fix the number of messages received in 
        while datetime.datetime.now() <= endTime:
            try:
                a,address=s.recvfrom(2048)
                a=a.decode()   
                if a=='y':
                    print('Someone is Confused!')
                    x+=1
            except socket.timeout:
                continue

        print(x)
    
def send_message(s):
    s.sendto('y'.encode(),('172.29.153.48',12343))



teacher()

