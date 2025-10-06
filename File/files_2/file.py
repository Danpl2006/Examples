poem = "some some\n"
poem += "time time\n"
poem += "fan fan\n"
poem += "van van\n"

file = open("poem.txt", 'w')
file.write(poem)
file.close()
file = open("poem.txt", 'r')
for line in file:
    print(line, end='')
file.close()

file = open('poem.txt', 'a')
file.write('(someone)')
file.close()
