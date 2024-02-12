from ctypes import *
import tkinter as tk
from threading import *
import time, os, sys, multiprocessing
from GPS_I2C import *
from COMS import *

#Global variables
mode = 0
start = 0

#This sets wheather this sends data or recieves data
def changeMode():
    #This would call the c functions
    global mode
    mode = ~mode
    # print("mode value:")
    # print(mode)
    if mode == 0:
        modeButton_text.set("Receiver")
    else:
        modeButton_text.set("Sender")  

def get_GPS():
    global start, mode
    start = ~start
    print(start)
    if start == 0:
        startButton_text.set("Start")
    else:
        startButton_text.set("Stop")
        if mode != 0: #Sender mode
            while start != 0:
                coords = getCoords() # grabs coordinates
                try:
                    lat = str(coords[0])
                    longit = str(coords[1])
                    print(coords)
                    sendData(lat + "," + longit)
                    latNum_text.set(lat)
                    longNum_text.set(longit)
                except:
                    continue
        else: #Receiver mode
            while start != 0:
                data = receiveData().split(",")
                print(data) 
                coords = getCoords()
                try:
                    latNum_text.set(data[2])
                    longNum_text.set(data[3])
                except:
                    continue

#This is the GUI
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs): #This part sets up the GUI
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("ECE Senior Design 2")
        self.geometry("500x400")
        # self.attributes('-zoomed', True)
        self.resizable(height=False, width=False)
        
        #Labels
        global latNum_text, longNum_text
        latNum_text, longNum_text = tk.StringVar(), tk.StringVar()
        Lat = tk.Label(self, text="Latitude:").place(x=100, y=100)
        latNum = tk.Label(self, textvariable=latNum_text).place(x=180, y=100)
        long = tk.Label(self, text="Longitude:").place(x=300, y=100)
        longNum = tk.Label(self, textvariable=longNum_text).place(x=380, y=100)
        latNum_text.set("0.0")
        longNum_text.set("0.0")
        
        #Buttons
        global modeButton_text, startButton_text
        modeButton_text, startButton_text = tk.StringVar(), tk.StringVar()
        modeButton = tk.Button(self, textvariable=modeButton_text, command=changeMode).place(x=0, y=370)
        modeButton_text.set("Receiver")
        
        tk.Button(self, textvariable=startButton_text, command= lambda: Thread(target=get_GPS, daemon=True).start()).place(x=220, y=160)
        startButton_text.set("Start")
    

#Main
if __name__ == "__main__":
    #This starts the GUI proccess
    display = GUI()
    display.mainloop()
    
    