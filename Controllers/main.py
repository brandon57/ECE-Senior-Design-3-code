from .mainpage import MainPage_Controller
from .settings import Settings_controller
from Views.main import View
from Model.main import Model
from COMS import parameters

class Main_Controller:
    # This creates everything
    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model
        
        self.mainpage_controller = MainPage_Controller(self, view, model)
        #self.settings_controller = Settings_controller(self, view, model)
        
        parameters("7,8,4,12")
        
        self.change_frame("mainpage")
        
        self.view.start_gui()
    
    # This changes what frame is being showed
    def change_frame(self, name: str):
        self.view.change_frame(name)
    
    