from threading import *
# from Views import display
# from .main import Main_Controller
from COMS import *
from GPS_I2C import getCoords
from Views.main import View #Testing

#Made a control class that helps manage the logic of the code. Also made a 

class MainPage_Controller():
    
    def __init__(self, main, view: View, model):
        self.main = main
        self.view = view
        self.model = model
        self.frame = self.view.frames["mainpage"]
        
        # self.start = False
        # self.mode = 0
        # self.user_coords = [0.0, 0.0]
        
        self.GPS = None
        self.stop_thread = Event()
    
    def start(self):
        if self.stop_thread:
            self.stop_thread.clear()
        self.model.change_start()
        # self.start = not self.start
        
        if self.model.get_start() == True:
            self.frame.update_start("Start")
            #startButton_text.set("Start")
            self.stop()
        else:
            self.frame.update_start("Stop")
            #startButton_text.set("Stop")
            if self.mode != 0:
                self.GPS = Thread(target=self.Sender, daemon=True).start()
            else:
                self.GPS = Thread(target=self.Receiver, daemon=True).start()
    
    def Sender(self):
        while not self.stop_thread.is_set():
            coords = getCoords() # grabs coordinates
            try:
                lat_diff = str(-(self.user_coords[0] - coords[0]))
                longit_diff = str(-(self.user_coords[1] - coords[1]))
                print(coords)
                # sendData(lat + "," + longit)
                if not self.stop_thread.is_set():
                    sendData(lat_diff + "," + longit_diff)
                    self.frame.update_coords(str(coords[0]), str(coords[1]))
                    # latNum_text.set(str(coords[0]))
                    # longNum_text.set(str(coords[1]))
            except:
                continue
    
    def Receiver(self):
        while not self.stop_thread.is_set():
            data = receiveData().split(",")
            print(data) #Testing
            
            coords = getCoords()
            try:
                lat = str(round(coords[0] - float(data[2]), 4))
                longit = str(round(coords[1] - float(data[3]), 4))
                print(lat + "," + longit) #Testing
                self.frame.update_coords(lat, longit)
                # latNum_text.set(lat)
                # longNum_text.set(longit)
            except:
                print("conversion error")
                continue
    
    def changeMode(self):
        self.mode = ~self.mode
        # print("mode value:")
        # print(mode)
        if self.mode == 0:
            self.frame.update_mode("Receiver")
            #modeButton_text.set("Receiver")
        else:
            self.frame.update_mode("Sender")
            #modeButton_text.set("Sender")
        
    def stop(self):
        self.stop_thread.set()
        self.GPS.join()
        self.GPS = None