from configparser import ConfigParser, ExtendedInterpolation
import os.path

class Model:
    def __init__(self):
        self.config = ConfigParser(interpolation=ExtendedInterpolation())
        self.config.optionxform = str
        if os.path.isfile('config.ini'):
            self.config.read('config.ini')
            # self.config.set('User', 'mode', '${DEFAULT:mode}')
        else:
            self.config['DEFAULT'] = {
            'mode': '0',
            'latitude': '0.0',
            'longitude': '0.0'
            }
            self.config['User'] = {
                'mode': '${DEFAULT:mode}',
                'latitude': '${DEFAULT:latitude}',
                'longitude': '${DEFAULT:longitude}'
            }
            
        self.write()
    
    def set_mode(self, mode):
        # mode = self.config.getint('User', 'mode')
        # mode = ~mode
        self.config.set('User', 'mode', str(mode))
        self.write()
        
    def get_mode(self):
        return self.config.getint('User', 'mode')
    
    def update_lat(self, lat):
        self.config.set('User', 'latitude', lat)
        self.write()
    
    def update_longit(self, longit):
        self.config.set('User', 'longitude', longit)
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
        self.config.set('User', 'mode', '${DEFAULT:mode}')
        self.config.set('User', 'latitude', '${DEFAULT:latitude}')
        self.config.set('User', 'longitude', '${DEFAULT:longitude}')
        self.write()