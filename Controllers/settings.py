# from main import Main_Controller


class Settings_controller():
    def __init__(self, main, view, model):
        self.main = main
        self.view = view
        self.model = model
        self.frame = self.view.frames["settings"]