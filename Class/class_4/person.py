class Person:
    '''BASE CLASS'''
    def __init__(self, name):
        self.name = name
    def speak(self, msg = "(Calling bse class)"):
        print(self.name, msg)
