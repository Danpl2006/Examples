from person import *
class Man(Person):
    ''' Производный CLASS'''
    def speak(self, msg):
        print(self.name,"\n\tHello!",  msg)