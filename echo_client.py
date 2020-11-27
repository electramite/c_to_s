import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
    	i = input("say something...")
    	s.sendall(str.encode(i))
    	data = s.recv(1024)
    	data.decode("utf-8")
    	print(f'Response from the server - {data}')



    
    

