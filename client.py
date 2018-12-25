import socket
serverip='10.20.30.241'
serverport=12000
BUFFER_SIZE=1024
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
    c = input('pleas input the price range you have :')  # inputing the price range of the user
    client.sendto(message.encode('utf-8'),(serverip,serverport))
    response,address=client.recvfrom(BUFFER_SIZE)
    print (message +'$'+''+'the computer stats you can affourd are : '+response.decode('utf-8'))

client.close()
