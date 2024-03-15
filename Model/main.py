from configparser import ConfigParser, ExtendedInterpolation

class Model:
    def __init__(self):
        self.config = ConfigParser(interpolation=ExtendedInterpolation())
        self.config['DEFAULT'] = {
        'start': 'False',
        'mode': '0',
        'latitude': '0.0',
        'longitude': '0.0'
        }
        
        self.config['User'] = {
            'start': '${DEFAULT:start}',
            'mode': '${DEFAULT:mode}',
            'latitude': '${DEFAULT:latitude}',
            'longitude': '${DEFAULT:longitude}'
        }
        
        self.write()
        
    def change_start(self):
        start = self.config.getboolean('User', 'start')
        start = not start
        self.config.set('User', 'start', str(start))
        self.write()
        
    def get_start(self):
        return self.config.getboolean('User', 'start')
    
    def change_mode(self):
        mode = self.config.getint('User', 'mode')
        mode = ~mode
        self.config.set('User', 'mode', str(mode))
        self.write()
        
    def get_mode(self):
        return self.config.getint('User', 'mode')
    
    def update_coords(self, lat, longit):
        self.config.set('User', 'latitude', str(lat))
        self.config.set('User', 'longitude', str(longit))
        self.write()
        
    def get_coords(self):
        coords = []
        coords.append(self.config.getfloat('User', 'latitude'))
        coords.append(self.config.getfloat('User', 'longitude'))
        return coords
    
    def write(self):
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
    
    def default(self):
        self.config.set('User', 'start', '${DEFAULT:start}')
        self.config.set('User', 'mode', '${DEFAULT:mode}')
        self.config.set('User', 'latitude', '${DEFAULT:latitude}')
        self.config.set('User', 'longitude', '${DEFAULT:longitude}')
        self.write()