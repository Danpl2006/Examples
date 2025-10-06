from person import *

class Hombre(Person):
    '''Class'''
    def speak(self, msg):
        print(self.name, "\n\thola!", msg)