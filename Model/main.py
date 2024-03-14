import configparser

class Model:
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config['DEFAULT'] = {
        'start': 'False',
        'mode': '0',
        'user_coords': '[0.0, 0.0]'
        }
        
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        
        #print(self.config.getboolean('DEFAULT', 'start'))
        
    def change_start(self):
        data["start"] = not data["start"]
        
    def get_start():
        return data["start"]
    
    def change_mode():
        data["mode"] = not data["mode"]
        
    def get_mode():
        return data["mode"]
    
    def update_coords(lat, longit):
        data["user_coords"] = [lat, longit]
        
    def get_coords():
        return data["user_coords"]
    
    