class Songbird:
    def __init__(self, name, song):
        self.name = name
        self.song = song
        print(self.name, "Is born...")

    def sing(self):
        print(self.name, "Sings: ", self.song)

    def __del__(self):
        print(self.name, "Flew away")
