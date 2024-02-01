import serial

device = serial.Serial("/dev/ttyS0", 115200, timeout=1)

AT_Command = "AT+SEND=101,41,"

# def setMode(input):
#     mode = input
    
def sendData(message):
    data = AT_Command + message
    device.write(data)
    
def receiveData():
    while True:
        message = device.readline.decode("utf-8")
        if len(message) != 0:
            return