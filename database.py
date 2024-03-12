
# import configparser

# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'start': 'False',
#     'mode': 0,
#     'user_coords': '[0.0, 0.0]'
# }

class Database:
    
    def __init__(self):
        self.data = {
            "start": False,
            "mode": 0,
            "user_coords": [0.0, 0.0]
        }
        
        # self.start = False
        # self.mode = 0
        # self.user_coords = [0.0, 0.0]
        
    def change_start(self):
        self.data["start"] = not self.data["start"]
        
    def get_start(self):
        return self.data["start"]
    
    def change_mode(self):
        self.data["mode"] = not self.data["mode"]
        
    def get_mode(self):
        return self.data["mode"]
    
    def update_coords(self, lat, longit):
        self.data["user_coords"] = [lat, longit]
        
    def get_coords(self):
        return self.data["user_coords"]
    
    