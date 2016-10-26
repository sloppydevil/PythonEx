#!python
import socket   
import commands  
import time 
HOST='0.0.0.0'
PORT=50007
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
s.bind((HOST,PORT))   
s.listen(1)         
while 1:

	conn,addr=s.accept()   
	print 'Connected by',addr  
	conn.settimeout(5)	
	while 1:
		try:
			print "=" * 32
			data = conn.recv(1024)  
			type(data)
			print data, " is received!"
			raw_val = data
			try:
				raw_val = int(data)
			except Exception:
				raw_val = 0xff 

			# business logic
			# time.sleep(3)
			
			ans = raw_val ** 2 
			print "-" * 16
			print ans," is sent!"
			raw_str = str(ans)
			conn.sendall(raw_str) 
		except socket.timeout, a:
			print a
		except:
			print "except"
			conn.close() 
			break
conn.close()     
