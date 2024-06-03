#cli_based.py  
#sender  # port limit0 to 65536
 #ip4 used for 32 and 64 bit
#ip 6 used for 32 bit
#ip_address= 192.168.0.171
#port = 8888
#exception as e is used to any error like syntax other
#sender

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address =  '192.168.0.182'
port = 8888
target= (ip_address,port)
message = input("kya message karoge")
message.encode('ascii')
encript_message = message.encode('ascii')
s.sendto(encript_message,target)
print("code is run")
#except Exception as e:
 #   print(" no need")












