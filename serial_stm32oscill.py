#!/usr/bin/python


import serial
from time import time_ns

# 921600
with serial.Serial('/dev/ttyACM0', 115200, timeout=10) as ser:
    try:
        dataLen = 2048//2
        valDataBuf = [None]*dataLen
        dataBufLen = 2*dataLen
        ser.reset_input_buffer()
        while (True):
            # if (ser.in_waiting < dataBufLen):
                # print("Waiting.")
                # continue
            dataBuf = ser.read(dataBufLen)
            for i in range(dataLen):
                valDataBuf[i] = dataBuf[2*i] + (dataBuf[2*i+1] << 8)
            # print(valDataBuf)
            print(len(valDataBuf))
            print(time_ns())
    except KeyboardInterrupt:
        print("Exiting.")

