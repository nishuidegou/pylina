import time
from websocket import create_connection
ws = create_connection("ws://192.168.0.101:8887/")
print ("Sending 'Hello, World'...")
for i in range(10, 20):
    time.sleep(1000)
    ws.send("Hello, World %s" % i)
    print ("Sent %s",  i)
    print ("Reeiving...%s",  i)
    result = ws.recv()
    print ("Received '%s'" % result)
time.sleep(30)
ws.close()