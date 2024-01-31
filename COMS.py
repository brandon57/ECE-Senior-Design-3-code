import serial


device = serial.Serial("/dev/ttyS0", 115200, timeout=1)
mode = 0

# def setMode(input):
#     mode = input
    
def sendData(message):
    device.write(message)
    
def receiveData():
    while True:
        message = device.readline.decode("utf-8")
        if len(message) != 0:
            return