class Settings_Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.frame = self.view.frames["settings"]

        self.configure()
        
    def configure(self): # Configures the buttons
        test = 0
        self.frame.back_button.configure(command=lambda: self.view.change_frame("mainframe"))
        self.frame.toggle_fullscreen_button.configure(command=self.view.toggle_fullscreen)
        self.frame.map_button.configure(command=lambda: self.view.change_frame("map"))
