from triangle import *
from rect import *

rect = Rect()
triangle = Triangle()

rect.set_values(7, 4)
triangle.set_values(7, 4)

print("Triangle ", triangle.area())
print("Rectangle", rect.area())