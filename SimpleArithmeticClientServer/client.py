
#python socket 

#client side 
import socket

def client_program():
    host = socket.gethostname()   
    port = 5000   
    message='hi'
    client_socket = socket.socket()   
    client_socket.connect((host, port))   

    message = input("Talk to server >>  ") 

    client_socket.send(str(message).encode()) 

    while message.lower()!='bye':



	    data = client_socket.recv(1024).decode() 
	    

	    print('server says :  ' + data) 

	    message = input("reply >>  ")
	    client_socket.send(str(message).encode()) 

        
    print("okay bye !")
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
