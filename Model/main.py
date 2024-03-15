import configparser

class Model:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config['DEFAULT'] = {
        'start': 'False',
        'mode': '0',
        'latitude': '0.0',
        'longitude': '0.0'
        }
        
        self.write()
        
        # print(self.config.get('DEFAULT', 'user_coords'))
        # print(self.get_start())
        
    def change_start(self):
        start = self.config.getboolean('DEFAULT', 'start')
        start = not start
        print(start)
        self.config.set('DEFAULT', 'start', str(start))
        
    def get_start(self):
        return self.config.getboolean('DEFAULT', 'start')
    
    def change_mode(self):
        mode = self.config.getint('DEFAULT', 'mode')
        print(mode)
        mode = ~mode
        self.config.set('DEFAULT', 'mode', str(mode))
        print(self.config.getint('DEFAULT', 'mode'))
        
    def get_mode(self):
        return self.config.getint('DEFAULT', 'mode')
    
    def update_coords(self, lat, longit):
        self.config.set('DEFAULT', 'latitude', str(lat))
        self.config.set('DEFAULT', 'longitude', str(longit))
        
    def get_coords(self):
        coords = []
        coords.append(self.config.getfloat('DEFAULT', 'latitude'))
        coords.append(self.config.getfloat('DEFAULT', 'longitude'))
        return coords
    
    def write(self):
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
    
    def default(self):
        test = 0