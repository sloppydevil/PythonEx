import socket
HOST='0.0.0.0'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
try:
	s.connect((HOST,PORT))  
	while 1:
		print "=" * 32
		num_value = input("enter a num:")
		print "%3d is sent!" % num_value
		num_str = str(num_value)
		s.sendall(num_str.encode("utf-8"))
		data=s.recv(1024)     
		print "%3d is received!" % int(data)   
	s.close()   
except Exception, error:
	print error

