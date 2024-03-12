# from main import Main_Controller


class Settings_controller():
    def __init__(self, main, view, database):
        self.main = main
        self.view = view
        self.frame = self.view.frames["settings"]