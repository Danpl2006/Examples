from songbird import *

bird_1 = Songbird("Koko", "TE-TE")
print(bird_1.name, "Id-", id(bird_1))
bird_1.sing()

del bird_1

bird_2 = Songbird("Lou", "Beee")
print(bird_2.name, "Id-", id(bird_2))
bird_2.sing()

bird_3 = Songbird("pou", "eee")
print(bird_3.name, "Id-", id(bird_3))
bird_3.sing()

del bird_2
del bird_3