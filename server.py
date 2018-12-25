import socket
#decompressing the message
def cmp(message):
    if int(message) >=0 and int(message)<=100 :
        return ('cpu:core 2d ,ram:2,hard:256gb,video card :200mb')
    elif int(message) >=100 and int(message)<=200:
        return("cpu:core i3 ,ram:2,hard:256gb,video card :512mb")
    elif int(message) >=200 and int(message)<=300 :
        return("cpu:core i3 ,ram:2,hard:500gb,video card :1gb")
    elif  int(message) >=300 and int(message)<=400 :
        return("cpu:core i5 ,ram:4,hard:500gb,video card :1gb")
    elif int(message) >=400 and int(message)<=500 :
        return("cpu:core i7 ,ram:6,hard:1000gb,video card :2gb")
    elif int(message) >=500 and int(message)<=600 :
        return("cpu:core i9 ,ram:6,hard:1000gb,video card :2gb")
    elif int(message) >=600 and int(message)<=700 :
        return("cpu:core i9 ,ram:8,hard:1000gb,video card :3gb")
    elif int(message) >=700 and int(message)<=800 :
        return("cpu:core i9 ,ram:10,hard:2000gb,video card :4gb")
    elif int(message) >=800 and int(message)<=900 :
        return("cpu:core i9 ,ram:14,hard:2000gb,video card :4gb")
    elif int(message) >=900 and int(message)<=1000 :
        return("cpu:core i9 ,ram:16,hard:3000gb,video card :4gb")
    else:
        return("im sorry we dont have iformation of a computer by this price")

serverport=12000
BUFFER_SIZE=1024
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind(('',serverport))
print('The server is ready to receive port 12800')
while 1:
    message,clientaddress=serversocket.recvfrom(BUFFER_SIZE)
    message=message.decode('utf-8')
    response=str(cmp(message))
    serversocket.sendto(response.encode('utf-8'),clientaddress)
    print('$'+str(response))