import serial
import time

try:
    device = serial.Serial("/dev/ttyS0", 115200, timeout=1)
except:
    print("Error: UART initalization failed")
    device = serial.Serial(None)

AT_Command = "AT+SEND=0,"
AT_Parameters = "AT+PARAMETER="

def parameters(message):
    data = AT_Parameters + message + "\r\n"
    try:
        device.write(data.encode("ASCII"))
    except:
        print("Unable to write parameters to UART.")

def sendData(message):
    data = AT_Command + str(len(message)) + "," +  message + "\r\n"
    try:
        device.write(data.encode("ASCII"))
    except:
        print("Unable to send message over UART.")
    
def receiveData():
    last_message = ''
    while True:
        try:
            while True:
                message = device.readline().decode("ASCII").replace('\r\n', '')
                if (len(message) == 0 or not message) and len(last_message) != 0:
                    break
                last_message = message
        except:
            print("Error reading message from UART.")
            return "error"
        
        try:
            return last_message
        except:
            print ("Error parsing message from UART.")
            return "error"

# if __name__ == '__main__':
#     test = 0
#     while True:
#         if test == 0: #receiver
#             print(receiveData())
#         else: #Sender
#             sendData("This is a test message")
#         time.sleep(3)