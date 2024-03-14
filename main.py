from Views.main import View
from Controllers.main import Main_Controller
from Model.main import Model
# from COMS import parameters

# display = Display

# def update_coords(lat, longit):
#     #global display
#     Display.MainPage.update_coords(lat, longit)
#     #Display.MainPage.longNum_text.set(longit)
    
# def update_start(text):
#     #global display
#     Display.MainPage.update_start(text)
#     #Display.MainPage.startButton_text.set(text)
    

# def update_mode(text):
#     #global display
#     Display.MainPage.update_mode(text)
#     #Display.MainPage.modeButton_text.set(text)
    
#Main
if __name__ == "__main__":
    #This starts the MainPage proccess
    # parameters("7,8,4,12")
    # display = Display.MainPage(parent=1)
    # display.mainloop()
    
    view = View()
    model = Model()
    controller = Main_Controller(view, model)