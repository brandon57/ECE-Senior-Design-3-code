import serial
import time

device = serial.Serial("/dev/ttyS0", 115200, timeout=1)

AT_Command = "AT+SEND=101,30,"
AT_Parameters = "AT+PARAMETER="

def parameters(message):
    data = AT_Parameters + message + "\r\n"
    try:
        device.write(data.encode("ASCII"))
    except:
        print("Unable to write parameters to UART.")

def sendData(message):
    data = AT_Command + message + "\r\n"
    try:
        device.write(data.encode("ASCII"))
    except:
        print("Unable to send message over UART.")
    
def receiveData():
    while True:
        message = device.readline().decode("ASCII").replace('\r\n', '')
        try:
            if len(message) != 0:
                return message
        except:
            return "Error reading message"

# if __name__ == '__main__':
#     test = 0
#     while True:
#         if test == 0: #receiver
#             print(receiveData())
#         else: #Sender
#             sendData("This is a test message")
#         time.sleep(3)