

class Map_Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.frame = self.view.frames["map"]
        self.configure()
        
        
    def configure(self): # Configures the buttons
        self.frame.main_button.config(command= lambda: self.view.change_frame("mainframe"))