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
        
        print(self.config.get('DEFAULT', 'user_coords'))
        print(self.get_start())
        
    def change_start(self):
        #self.config.
        data["start"] = not data["start"]
        
    def get_start(self):
        return self.config.getboolean('DEFAULT', 'start')
    
    def change_mode(self):
        data["mode"] = not data["mode"]
        
    def get_mode(self):
        return self.config.getint('DEFAULT', 'mode')
    
    def update_coords(self, lat, longit):
        data["user_coords"] = [lat, longit]
        
    def get_coords(self):
        return self.config.get('DEFAULT', 'user_coords')
    
    