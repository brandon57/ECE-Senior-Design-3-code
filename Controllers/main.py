from .mainframe import MainFrame_Controller
from .settings import Settings_Controller
from .map import Map_Controller
from Views.main import View
from Model.main import Model
from IO.COMS import parameters

class Main_Controller:
    # This creates everything
    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model
        
        self.mainframe_controller = MainFrame_Controller(view, model)
        self.settings_controller = Settings_Controller(view, model)
        self.map_controller = Map_Controller(view, model)
        
        parameters("7,8,4,12")
        
        self.view.change_frame("mainframe")
        
        self.view.start_gui()