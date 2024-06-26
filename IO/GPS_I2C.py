import smbus2
import time

bus = smbus2.SMBus(1)
address = 0x42

checkSumTable = ["A*60", "A*61", "A*62", "A*63" "A*64", "A*65", "A*66", "A*67", "A*68", "A*69", "A*6A", "A*6B", "A*6C", "A*6D", "A*6E", "A*6F"]

# Takes the GPS data and converts it to latitude and longitude
def getCoords():
    results = []
    last_success = time.time_ns()
    last_attempt = time.time_ns()
    while last_attempt - last_success < 3000000000:
        last_attempt = time.time_ns()      
        message = grabGPSData()
        if message != []:
            try:
                if message[0][3:6] == "GLL":
                    latDMS = float(message[1])
                    longDMS = float(message[3])
                    latDir = message[2]
                    longDir = message[4]
                elif message[0][3:6] == "RMC":
                    latDMS = float(message[3])
                    longDMS = float(message[5])
                    latDir = message[4]
                    longDir = message[6]

                if len(latDir) == 1 and len(longDir) == 1:
                    latMin = DegMinConverter(int(latDMS/100), latDMS - (100*int(latDMS/100)), latDir)
                    longMin = DegMinConverter(int(longDMS/100), longDMS - (100*int(longDMS/100)), longDir)
                    results.append(latMin)
                    results.append(longMin)
                    last_success = time.time_ns()
                    return results
            except:
                print("error getting coords")
                results.clear()
                continue
    print("Nothing to read from GPS.")
    return []
    
# Grabs the correct GPS message
def grabGPSData():
    GPS_Message = []
    GPS = ""
    last_success = time.time_ns()
    last_attempt = time.time_ns()
    while last_attempt - last_success < 1000000000:
        last_attempt = time.time_ns()
        data = chr(bus.read_byte(address))
        if data == '$':
            GPS_Message.append(data)
            while True:
                data = chr(bus.read_byte(address))
                if data != '\r':
                    GPS_Message.append(data)
                else:
                    break
        if len(GPS_Message) != 0:
            temp = [x for x in GPS_Message]
            GPS = ''.join(temp).strip().split(",")
            try:
                if GPS[0][3:6] == "GLL" and GPS[6] == 'A':
                    print(GPS)
                    last_success = time.time_ns()
                    return GPS
                elif GPS[0][3:6] == "RMC" and GPS[2] == 'A':
                    print(GPS)
                    last_success = time.time_ns()
                    return GPS
            except:
                print("Message not fully filled in")
                continue
            GPS_Message.clear()
            time.sleep(0.05)
    return []
            
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