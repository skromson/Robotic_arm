import numpy

#class defining robots logic
class Robot():
    def __init__(self, phi, zHeight, rExtension):
        self.__phi = self.phi
        self.__zHeight = self.zHeight
        self.__rExtension = self.rExtension
    
    #setting bounds to phi
    @property.setter
    def phi(self, angle):
        if angle < -170:
            set.__phi = -170
        if angle > 170:
            set.__phi = 170
    
    #setting bounds to zHeight
    @property.setter
    def zHeight(self, height):
        if height < 0:
            self.__zHeight = 0
        if height > 100:
            self.__zHeight = 100
    
    #setting bounds to rExtension
    @property.setter
    def rExtension(self, extension):
        if extension < 0:
            self.__rExtension = 0
        if extension > 50:
            self.__rExtension = 50
    
    #getters
    @property
    def phi(self):
        return self.__phi
    @property
    def zHeight(self):
        return self.__zHeight
    @property
    def rExtension(self):
        return self.__rExtension
    
    