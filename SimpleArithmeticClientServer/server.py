
#server side socket implementation 

import socket 

def server_program():
    # getting the hostname
    host = socket.gethostname()
    port = 5000  
    a=0
    
    opt='hi'
    reply=''
    server_socket = socket.socket()  

    
    server_socket.bind((host, port))  

    
    server_socket.listen(2)

    conn, address = server_socket.accept()

    print("Connection from: " + str(address))
    mm=conn.recv(1024).decode()
    print(mm)

    while opt!='bye'or reply!='bye':

    	

    	que="\n select any option   \n 1 : for  addition  \n 2 : for substraction \n 3 : for multiplication \n bye:for exit"
    	data=conn.send(que.encode())
    	opt=conn.recv(1024).decode()
    	print("from client: option recieved  " + str(opt))

    	if str(opt)=='bye' or str(reply)=='bye':
    		print("sorry connection closed")
	    	conn.close()
	    	break
	    
	    
    	conn.send("enter the first number".encode())
    	a=conn.recv(1024).decode()
	    	

    	conn.send("enter the second number".encode())
    	b=conn.recv(1024).decode()


    	if int(opt)==1:
	    	print("performing addition")
	    	
	    	c=int(a)+int(b)
	    	sendi="the addition of numbers is >> "+str(c)
	    	conn.send(sendi.encode())
	    	reply=conn.recv(1024).decode()

	    	print("addition carried out successfully")
	    	 
	    	


    	if int(opt)==2:
    		print("performing substraction")
	    	
	    	c=int(a)-int(b)
	    	sendi="the substraction of numbers is >> "+str(c)
	    	conn.send(sendi.encode())

	    	print("substraction carried out successfully")
	    	 
	    	reply=conn.recv(1024).decode()
	    	
    	if int(opt)==3:
	    	print("performing multiplication")
	    	
	    	c=int(a)*int(b)
	    	sendi="the multiplication of numbers is >> "+str(c)
	    	conn.send(sendi.encode())
	    	reply=conn.recv(1024).decode()



	    	print("multiplication carried out successfully")
	    	 
    conn.close()
    	


if __name__ == '__main__':
    server_program()