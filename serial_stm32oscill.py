#!/usr/bin/python


# ----------/ CONFIG \-----------

devPath = '/dev/ttyACM0'

# [seconds]
devReadTimeout = 10

'''
    The sampling frequency of STM ADC. If multiple channels are sampled, 
    this sets a time interval between measurements of group of channels.
    If the specified value can't be set due to a hardware restrictions,
    the nearest possible value will be used.

    dT = 1/sampFreq;   ch.1,2,3;

    1,2,3 ---> dT ---> 1,2,3 ---> dT ---> ...

    (The delay between measurements of an individual channels inside of the group 
    is set by a hardware; usually it is the smallest possible)

    [Hz]
'''
sampFreq = 1e4

'''
    How frequently STM data buffer is transmitted to PC (not the USB packets).
    STM will take this value into consideration but it is not guaranteed to be obeyed
    if STM capabilities does not allow to do this. In the last case the nearest possible
    value will be used.

    [Hz]
'''
txFreq = 1/8

# ----------\ CONFIG /-----------


import serial
from time import time_ns


with serial.Serial(devPath, timeout=devReadTimeout) as ser:
    try:
        # Set config
        # ser.write()
        dataBufLen = 2048
        dataLen = dataBufLen//2
        valDataBuf = [None]*dataLen
        # ser.reset_input_buffer()
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

