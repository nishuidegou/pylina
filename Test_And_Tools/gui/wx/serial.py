import serial
from threading import Thread
import re
import wx
import time
import os
import binascii

Flag = True

def readLinesFromFile():
    wxApp = wx.PySimpleApp()
    wildcard = "test file (*.txt)|*.txt|"\
            "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        fopen = open(dialog.GetPath(), "r")
        lines = fopen.readlines()
        fopen.close()

        dialog.Destroy()
        return lines
    else:
        dialog.Destroy()
        return None



def serailWriteThread(ser, lines):

    for line in lines:
        line = lineSplit(line)
        # print(line)
        for cmd in line:
            if re.match('delay', cmd):
                d = re.sub("\D", "", cmd)
                # print(d)
                time.sleep(int(d))
            else:
                hexCmd = binascii.a2b_hex(cmd)
                # print(hexCmd)
                ser.write(hexCmd)

            time.sleep(0.005)

    # Flag = False



def serialReadThread(ser):

    while True:
        rx = ser.read()
        r = binascii.b2a_hex(rx)
        rxStr = r.decode("utf-8")
        print("rx thread:",rxStr )
        fopen = open('./output.txt', 'a')
        fopen.write(rxStr + ' ')
        fopen.close()
        # if Flag == False:
        #     fopen.close()


def lineSplit(line):

    line = line.strip('\n')
    # print(line)
    line_s = re.split(' ', line)
    # if '\n' in line_s:
    #     line_s.remove('\n')
    # print(line_s)
    return line_s


if __name__ == '__main__':
    cmdLines = []

    lines = readLinesFromFile()
    # print((lines))
    portConfig = lineSplit(lines[1])
    print(portConfig,'command delay 5ms')
    ser = serial.Serial(portConfig[0],portConfig[1])

    lines = lines[2:]
    for line in lines:
        if '#' not in line:
            cmdLines.append(line)
    # print(cmdLines)

    rxThread = Thread(target=serialReadThread,args=[ser])
    txThread = Thread(target=serailWriteThread,args=[ser,cmdLines])

    try:
        os.remove('./output.txt')
    except FileNotFoundError as e:
        print(e)

    txThread.start()
    # time.sleep(0.5)
    rxThread.start()



