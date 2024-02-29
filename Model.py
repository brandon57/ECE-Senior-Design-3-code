import Display
from COMS import parameters

display = Display

def update_coords(lat, longit):
    #global display
    Display.GUI.update_coords(lat, longit)
    #Display.GUI.longNum_text.set(longit)
    
def update_start(text):
    #global display
    Display.GUI.update_start(text)
    #Display.GUI.startButton_text.set(text)
    

def update_mode(text):
    #global display
    Display.GUI.update_mode(text)
    #Display.GUI.modeButton_text.set(text)
    
#Main
if __name__ == "__main__":
    #This starts the GUI proccess
    parameters("7,8,4,12")
    display = Display.GUI()
    display.mainloop()