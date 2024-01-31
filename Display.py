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

# def GPS():
#     # global start
#     # start = ~start
#     GPS_thread = Thread(target=get_GPS).start()

def get_GPS():
    global start
    start = ~start
    if start != 0:
        startButton_text.set("Start")
    else:
        startButton_text.set("Stop")
    while start == 0:
        coords = getCoords()
        try:
            print(coords)
            latNum_text.set(str(coords[0]))
            longNum_text.set(str(coords[1]))
        except:
            continue

# def startProg():
#     #Starts the GPS and COMS
#     global start
#     start = ~start
#     # print("start value:")
#     # print(start)
#     if start == 0:
#         startButton_text.set("Start")
#     else:
#         result = getCoords()
#         latNum_text.set(str(result[0]))
#         longNum_text.set(str(result[1]))
#         startButton_text.set("Stop")

#This is the GUI
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #This part sets up the GUI
        # global display
        # display = tk.Tk()
        self.title("ECE Senior Design 2")
        self.geometry("500x400")
        # self.attributes('-zoomed', True)
        self.resizable(height=False, width=False)
        # L1 = tk.Label(display, text="X:")
        # L1.place(x=100, y=100)
        # L2 = tk.Label(display, text="Y:")
        # L2.place(x=300, y=100)
        
        # global E1
        # E1 = tk.Entry(display, bd = 3, width=10)
        # E1.place(x=100, y=125)
        # global E2
        # E2 = tk.Entry(display, bd = 3, width=10)
        # E2.place(x=300, y=125)
        
        #Labels
        global latNum_text, longNum_text
        latNum_text, longNum_text = tk.StringVar(), tk.StringVar()
        Lat = tk.Label(self, text="Latitude:").place(x=100, y=100)
        latNum = tk.Label(self, textvariable=latNum_text).place(x=180, y=100)
        long = tk.Label(self, text="Longitude:").place(x=300, y=100)
        longNum = tk.Label(self, textvariable=longNum_text).place(x=380, y=100)
        latNum_text.set("0.0")
        longNum_text.set("0.0")
        
        #Text
        
        
        #Buttons
        global modeButton_text, startButton_text
        modeButton_text, startButton_text = tk.StringVar(), tk.StringVar()
        modeButton = tk.Button(self, textvariable=modeButton_text, command=changeMode).place(x=0, y=370)
        modeButton_text.set("Receiver")
        
        tk.Button(self, textvariable=startButton_text, command= lambda: Thread(target=get_GPS, daemon=True).start()).place(x=220, y=160)
        startButton_text.set("Start")
        

# def GUI():
#     #This part sets up the GUI
#     # global display
#     display = tk.Tk()
#     display.title("ECE Senior Design 2")
#     display.geometry("500x400")
#     display.resizable(height=False, width=False)
#     # L1 = tk.Label(display, text="X:")
#     # L1.place(x=100, y=100)
#     # L2 = tk.Label(display, text="Y:")
#     # L2.place(x=300, y=100)
    
#     # global E1
#     # E1 = tk.Entry(display, bd = 3, width=10)
#     # E1.place(x=100, y=125)
#     # global E2
#     # E2 = tk.Entry(display, bd = 3, width=10)
#     # E2.place(x=300, y=125)
    
#     #Labels
#     global latNum_text, longNum_text
#     latNum_text, longNum_text = tk.StringVar(), tk.StringVar()
#     Lat = tk.Label(display, text="Latitude:").place(x=100, y=100)
#     latNum = tk.Label(display, textvariable=latNum_text).place(x=180, y=100)
#     long = tk.Label(display, text="Longitude:").place(x=300, y=100)
#     longNum = tk.Label(display, textvariable=longNum_text).place(x=380, y=100)
#     latNum_text.set("0.0")
#     longNum_text.set("0.0")
    
#     #Text
    
    
#     #Buttons
#     global modeButton_text, startButton_text
#     modeButton_text, startButton_text = tk.StringVar(), tk.StringVar()
#     modeButton = tk.Button(display, textvariable=modeButton_text, command=changeMode).place(x=0, y=370)
#     modeButton_text.set("Receiver")
    
#     tk.Button(display, textvariable=startButton_text, command=startProg).place(x=220, y=160)
#     startButton_text.set("Start")
    
#     #This starts the GUI
#     display.mainloop()
    

#Main
if __name__ == "__main__":
    # device = 's'
    # global so_file
    # global IO_functions
    # so_file = "./IO.so"
    # IO_functions = CDLL(so_file)
    # IO_functions.COMS_Startup(device, 115200)
    # IO_functions.GPS_Startup(1, 0x42)
    
    #This starts the GUI proccess
    display = GUI()
    display.mainloop()
    # UI = multiprocessing.Process(target=GUI)
    # UI.start()
    
    # UI.join()
    
    