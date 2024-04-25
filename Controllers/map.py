

class Map_Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.frame = self.view.frames["map"]
        # coords = self.model.get_coords()
        # self.frame.map_widget.set_position(coords[0], coords[1])
        self.frame.map_widget.set_position(46.0, -96.0)
        
        self.configure()
        
    def configure(self): # Configures the buttons
        self.frame.main_button.configure(command= lambda: self.view.change_frame("mainframe"))