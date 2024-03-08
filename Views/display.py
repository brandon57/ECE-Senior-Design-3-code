from ctypes import *
import tkinter as tk
from tkinter import ttk
from threading import *
import time, os, sys, multiprocessing
# from GPS_I2C import *
# from COMS import *

#Global variables
# mode = 0
# start = 0
# user_coords = [0.0, 0.0]

# This calculates the offset
# def offset(GPS_lat, GPS_long):
#     result = []
#     result[0] = user_coords[0] - GPS_lat
#     result[1] = user_coords[1] - GPS_long
#     return result

# This sets wheather this sends data or recieves data
# def changeMode():
#     global mode
#     mode = ~mode
#     # print("mode value:")
#     # print(mode)
#     if mode == 0:
#         modeButton_text.set("Receiver")
#     else:
#         modeButton_text.set("Sender")

# def get_GPS():
#     global start, mode, user_coords
#     start = ~start
#     print(start)
#     if start == 0:
#         startButton_text.set("Start")
#     else:
#         startButton_text.set("Stop")
#         if mode != 0: #Sender mode
#             while start != 0:
#                 coords = getCoords() # grabs coordinates
#                 try:
#                     lat_diff = str(-(user_coords[0] - coords[0]))
#                     longit_diff = str(-(user_coords[1] - coords[1]))
#                     print(coords)
#                     sendData(lat_diff + "," + longit_diff)
#                     # sendData(lat + "," + longit)
#                     latNum_text.set(str(coords[0]))
#                     longNum_text.set(str(coords[1]))
#                 except:
#                     continue
#         else: #Receiver mode
#             while start != 0:
#                 data = receiveData().split(",")
#                 print(data)
#                 # print(float(data[2]) + "," + float(data[3]))
#                 coords = getCoords()
#                 try:
#                     lat = str(round(coords[0] - float(data[2]), 4))
#                     longit = str(round(coords[1] - float(data[3]), 4))
#                     print(lat + "," + longit)
#                     latNum_text.set(lat)
#                     longNum_text.set(longit)
#                 except:
#                     print("conversion error")
#                     continue

# class Window(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         control = controller.Controller()
#         self.mainpage = MainPage(self, control)
#         self.settings = Settings(self, control)

#This is the GUI
class MainPage(tk.Frame):
    def __init__(self, controller): #This part sets up the GUI
        tk.Frame.__init__(self)
        # self.title("ECE Senior Design 2")
        # self.geometry("500x400")
        # # self.attributes('-zoomed', True)
        # self.resizable(height=False, width=False)
        self.controller = controller
        # control = controller.Controller()
        
        
        #Tabs
        # Tabs = ttk.Notebook(self)
        # self = ttk.Frame(Tabs)
        # tab2 = ttk.Frame(Tabs)
        # Tabs.add(self, text="test")
        # Tabs.add(tab2, text="Settings")
        # Tabs.pack(expand=1, fill='both')
        # ttk.Label(tab2, text="This is the settings").place(x=100, y=100)
        
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
        global modeButton_text, startButton_text, settingsButton_text
        modeButton_text, startButton_text, settingsButton_text = tk.StringVar(), tk.StringVar(), tk.StringVar()
        modeButton = tk.Button(self, textvariable=modeButton_text, command=controller.changeMode).place(x=0, y=370)
        modeButton_text.set("Receiver")
        
        # tk.Button(self, textvariable=startButton_text, command= lambda: Thread(target=get_GPS, daemon=True).start()).place(x=220, y=160)
        tk.Button(self, textvariable=startButton_text, command= control.start).place(x=220, y=160)
        startButton_text.set("Start")
        
        #setting = tk.Button(self, textvariable=settingsButton_text, command=self.settings.tkraise).place(x=300, y=200)
        
    def update_coords(lat, longit):
        #global display
        latNum_text.set(lat)
        longNum_text.set(longit)
    
    def update_start(text):
        #global display
        startButton_text.set(text)
        
    def update_mode(text):
        #global display
        modeButton_text.set(text)

# #Main
# if __name__ == "__main__":
#     #This starts the GUI proccess
#     controll = Control()
#     display = GUI()
#     display.mainloop()
    
    