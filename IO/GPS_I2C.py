import smbus2
import time

bus = smbus2.SMBus(1)
address = 0x42

checkSumTable = ["A*60", "A*61", "A*62", "A*63" "A*64", "A*65", "A*66", "A*67", "A*68", "A*69", "A*6A", "A*6B", "A*6C", "A*6D", "A*6E", "A*6F"]

# Takes the GPS data and converts it to latitude and longitude
def getCoords():
    # results = ""
    results = []
    message = grabGPSData()
    try:
        latDMS = float(message[1])
        longDMS = float(message[3])
        latMin = DegMinConverter(int(latDMS/100), latDMS - (100*int(latDMS/100)), message[2])
        longMin = DegMinConverter(int(longDMS/100), longDMS - (100*int(longDMS/100)), message[4])
        # latMin = DegMinConverter(latDMS[0:2], latDMS[2:10], message[2])
        # longMin = DegMinConverter(longDMS[0:3], longDMS[3:11], message[4])
        # print("Latitude:", latMin, ", Longitude:", longMin)
        results.append(latMin)
        results.append(longMin)
        # results = str(latMin) + "," + str(longMin)
        return results
    except:
        print("error")
        
    
# Grabs the correct GPS message
def grabGPSData():
    GPS_Message = []
    GPS = ""
    # checkSumGood = False
    while True:
        data = bus.read_byte(address)
        if chr(data) == '$':
            GPS_Message.append(chr(data))
            while True:
                temp = chr(bus.read_byte(address))
                if temp != '\r':
                    GPS_Message.append(temp)
                else:
                    break
        if len(GPS_Message) != 0:
            temp2 = [x for x in GPS_Message]
            GPS = ''.join(temp2).strip().split(",")
            # name = GPS[0]
            # print(GPS)
            if GPS[0] == "$GNGLL" and GPS[6] == 'A' and GPS[7] in checkSumTable:
                # checkSum = GPS[7]
                # if GPS[7] in checkSumTable:
                print(GPS)
                return GPS
                # for x in checkSumTable:
                #     if checkSum == x:
                #         # checkSumGood = True
                #         print(GPS)
                #         return GPS
                # print(GPS)
                # return GPS
            GPS_Message = []
            # time.sleep(600/1000) #Used for testing

def DegMinConverter(degrees, minutes, direction):
    result = degrees + (minutes/60)
    
    if (direction == 'W') | (direction == 'S'):
        result = -result
    return result

# For testing
# if __name__ == '__main__':
#     # global so_file
#     # global GPS_functions
#     # so_file = "./CPython.so"
#     # GPS_functions = CDLL(so_file)
#     while True:
#         getCoords()
#         # print(list)