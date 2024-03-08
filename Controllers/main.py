from mainpage import MainPage_Controller
from settings import Settings_controller

class Main_Controller:
    # This creates everything
    def __init__(self, view):
        self.view = view
    
    # This changes what frame is being showed
    def show_page(self):
        self.view.