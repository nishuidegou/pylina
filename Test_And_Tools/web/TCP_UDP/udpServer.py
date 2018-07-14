from socket import *
from time import ctime
import pyaudio

HOST = '192.168.0.1'
PORT = 
BUFSIZ = 128
ADDR = (HOST, PORT)

# 创建一个服务器端UDP套接字
udpServer = socket(AF_INET, SOCK_DGRAM)
# 绑定服务器套接字
udpServer.bind(ADDR)

while True:
    print('waiting for message...')
    # 接收来自客户端的数据
    data, addr = udpServer.recvfrom(BUFSIZ)
    print(data)
    # 向客户端发送数据
    udpServer.sendto(data,addr)
    print('...received from and returned to:', addr)

udpServer.close()