

class Settings_Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.frame = self.view.frames["settings"]
        
    def configure(self): # Configures the buttons
        test = 0