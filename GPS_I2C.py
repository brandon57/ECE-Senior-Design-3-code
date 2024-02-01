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
    latDMS = message[1]
    longDMS = message[3]
    try:
        latMin = DegMinConverter(latDMS[0:2], latDMS[2:10], message[2])
        longMin = DegMinConverter(longDMS[0:3], longDMS[3:11], message[4])
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
    checkSumGood = False
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
            name = GPS[0]
            # print(GPS)
            if name == "$GNGLL" and GPS[6] == 'A':
                checkSum = GPS[7]
                for x in checkSumTable:
                    if checkSum == x:
                        # checkSumGood = True
                        print(GPS)
                        return GPS
                # print(GPS)
                # return GPS
            GPS_Message = []
            # time.sleep(600/1000) #Used for testing

def DegMinConverter(degrees, minutes, direction):
    result = float(degrees) + (float(minutes)/60)
    
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
        
        
        
#         # print(data)
#         # if data[0] != 255:
#         #     data = ord(str(data))
#         #     print(data)
#         # if x == "$GNRMC":
#         #      if x  == "A":
#         #          print("e")
#                 #  latitude = data[3]
#                 #  latDir = data[4]
#                 #  longitude = data[5]
#                 #  longDir = data[6]
#                  #latitude = DegMinConverter(latitude[0:2], latitude[2:10], latDir)
#                  #longitude = DegMinConverter(longitude[0:3], longitude[3:11], longDir)
#                  #latitude = GPS_functions.DegMinConverter(int(latitude[0:2]), c_float(float(latitude[2:10])), longDir)
#                  #longitude = GPS_functions.DegMinConverter(int(longitude[0:3]), c_float(float(longitude[3:11])), latDir)
#                  #print(data)
#                  #print(data[0] + ", Latitude: " + str(latitude) + ", Longitude: " + str(longitude) + ", taken at: " + data[1] + " UTC")