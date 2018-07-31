#coding=utf-8
import serial, time
portnum = "/dev/ttyUSB0"


#port = serial.Serial(portnum)
#port.setTimeout(1)
        

#baudRate = 19200
#port.setTimeout(0.4)
#port.setBaudrate(19200)

"""
пусть надо послать два байта ШИМ
    a7 a6 a5 a4 a3 a2 a1 a0
    b7 b6 b5 b4 b3 b2 b1 b0
    тогда посылаются следующие 4 байта
    1  0  0  0    0  0  0  1   - адрес
    0  0  0  0    0  0 a0 b0
    0 a7 a6 a5   a4 a3 a2 a1
    0 b7 b6 b5   b4 b3 b2 b1
        
"""
def binary(n, digits=8):
    rep = bin(n)[2:]
    return ('0' * (digits - len(rep))) + rep



for v in range(255):
    a = v
    b = v
    chars = [0] * 4
    chars[0] = 0x81
    chars[1] = (a % 2) * 2 + b % 2
    chars[2] = a / 2
    chars[3] = b / 2
    
    print "speed = ", v, map(binary, chars), chars
    #continue
    cmd = chars
    cmd = map(lambda x:chr(x), cmd)
    cmd = "".join(cmd)
    #port.write(cmd)
    #data = port.read(5)
    #time.sleep(0.1)
        #print data
    
