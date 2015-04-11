import socket

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

    while True:

    	a=s.recvfrom(2048)
    	a=a.decode()
    	if a=='y':
    		print('Someone is Confused!')

def main():

	teacher_address=

	c=input('Student : s \n Teacher : t')
	if c =='s':
		student(teacher_address)
	if c=='t':
		teacher()

