import sys
from .mainframe import MainFrame_Controller
from Views.main import View
from Model.main import Model
from IO.COMS import parameters

class Main_Controller:
    # This creates everything
    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model
        
        self.mainframe_controller = MainFrame_Controller(view, model)
        
        parameters("10,9,4,6")
        
        self.view.change_frame("mainframe")
        
        self.view.start_gui()