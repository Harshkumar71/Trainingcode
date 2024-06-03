import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address =  '192.168.231.1'
port = 8888
complete_add = (ip_address,port)
s.bind(complete_add)
while True:
    message = s.recvfrom(120)
    print(message)
    data = message[0]
    data = '\n'
    print(data.encode('ascii'))
#except Exception as e:
 #   print("hello sir mene message receive kar liya h")

