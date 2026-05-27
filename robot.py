import numpy

#class defining robots logic
class Robot():
    def __init__(self):
        self.__phi = 0
        self.__zHeight = 50
        self.__rExtension = 10
    
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
    
    #setting bounds to phi
    @phi.setter
    def phi(self, angle):
        if angle < -170:
            self.__phi = -170
        elif angle > 170:
            self.__phi = 170
        else:
            self.__phi = angle
    
    #setting bounds to zHeight
    @zHeight.setter
    def zHeight(self, height):
        if height < 0:
            self.__zHeight = 0
        elif height > 100:
            self.__zHeight = 100
        else:
            self.__zHeight = height
    
    
    #setting bounds to rExtension
    @rExtension.setter
    def rExtension(self, extension):
        if extension < 0:
            self.__rExtension = 0
        elif extension > 50:
            self.__rExtension = 50
        else:
            self.__rExtension = extension
    