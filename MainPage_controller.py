from threading import *
import Model
import Display
from main_controller import Main_controller
from COMS import *
from GPS_I2C import getCoords

mode = 0

#Made a control class that helps manage the logic of the code. Also made a 

#global start, mode, user_coords

def changeMode():
    global mode
    mode = ~mode
    # print("mode value:")
    # print(mode)
    if mode == 0:
        Display.MainPage.update_mode("Receiver")
        #modeButton_text.set("Receiver")
    else:
        Display.MainPage.update_mode("Sender")
        #modeButton_text.set("Sender")

class mainpage_Controller(Main_controller):
    start = False
    user_coords = [0.0, 0.0]
    
    def __init__(self):
        #global mode, start, user_coords
        # mode = 0
        # Control.start = 0
        # user_coords = [0.0, 0.0]
        self.GPS = None
        self.stop_thread = Event()
        Main_controller.show_page
    
    def start(self):
        if self.stop_thread:
            self.stop_thread.clear()
        Controller.start = not Controller.start
        if Controller.start == True:
            Model.update_start("Start")
            #startButton_text.set("Start")
            self.stop()
        else:
            Model.update_start("Stop")
            #startButton_text.set("Stop")
            if mode != 0:
                self.GPS = Thread(target=self.Sender, daemon=True).start()
            else:
                self.GPS = Thread(target=self.Receiver, daemon=True).start()
    
    def Sender(self):
        while not self.stop_thread.is_set():
            coords = getCoords() # grabs coordinates
            try:
                lat_diff = str(-(Controller.user_coords[0] - coords[0]))
                longit_diff = str(-(Controller.user_coords[1] - coords[1]))
                print(coords)
                # sendData(lat + "," + longit)
                if not self.stop_thread.is_set():
                    sendData(lat_diff + "," + longit_diff)
                    Model.update_coords(str(coords[0]), str(coords[1]))
                    # latNum_text.set(str(coords[0]))
                    # longNum_text.set(str(coords[1]))
            except:
                continue
    
    def Receiver(self):
        while not self.stop_thread.is_set():
            data = receiveData().split(",")
            print(data)
            # print(float(data[2]) + "," + float(data[3]))
            coords = getCoords()
            try:
                lat = str(round(coords[0] - float(data[2]), 4))
                longit = str(round(coords[1] - float(data[3]), 4))
                print(lat + "," + longit)
                Model.update_coords(lat, longit)
                # latNum_text.set(lat)
                # longNum_text.set(longit)
            except:
                print("conversion error")
                continue
        
    def stop(self):
        self.stop_thread.set()
        #self.GPS.join()
        self.GPS = None