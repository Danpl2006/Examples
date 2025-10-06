import sys, keyword

print("V==", sys.version)

print("Loc", sys.executable)

for dir in sys.path:
    print(dir)


for word in keyword.kwlist:
    print(word)