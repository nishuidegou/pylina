import wx
import os
import serial
import time
import re
import binascii
import threading

# class pySer(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.setDeamn(True)
#         self.stateFlag=False
#         self.ser=serial.Serial("COMx",9600)
#     def run(self):
#         self.stateFlag=True
#         while(self.stateFlag):
#             if(self.ser.available()>0):
#                 time.sleep(0.05)
#                 self.task(self.ser.read(self.ser.available()))
#     def stop(self):
#         self.stateFlag=False
#     def task(self,data):
#
#     def write(self,data):
#         self.ser.write(data)


def Parse(filePath):
    fopen = open(filePath)
    t = fopen.read()
    s = re.split(' ',t)
    # print(type(s))
    # print(s[0],s[1])
    fopen.close()
    port = serial.Serial(s[0],s[1])
    c_list = s[2:]
    output = filePath + 'output.txt'
    fopen = open(output,'w')
    print(c_list)
    for command in c_list:
        # print(command)
        if re.match('delay',command):
            d = re.sub("\D", "", command)
            # print(d)
            time.sleep(int(d))
        else:
            print(command)
            port.write(binascii.a2b_hex(command))
            # n = port.write(bytes.fromhex(command))
            # time.sleep(0.05)
            # bufSize = port.inWaiting()
            # print(command,bufSize)
            # r = bytes.decode(port.read(2))
            # print(r)
            # fopen.write(r + " ")
            # if bufSize != 0:
            #     r = bytes.decode(port.read(bufSize))
            #     print(r)
            #     fopen.write(r + " ")
        time.sleep(0.05)

    time.sleep(0.05)
    bufSize = port.inWaiting()
    r = binascii.b2a_hex(port.read(bufSize))
    inStr = r.decode("utf-8")
    pattern = re.compile('.{1,2}')
    inStr = ' '.join(pattern.findall(inStr))
    print(bufSize)
    print(inStr)
    fopen.write(inStr)
    fopen.close()



if __name__ == '__main__':
    app = wx.PySimpleApp()
    wildcard = "test file (*.txt)|*.txt|"\
            "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        Parse(dialog.GetPath())

    dialog.Destroy()