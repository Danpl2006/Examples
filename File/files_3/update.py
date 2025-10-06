text = "The some words can always change someone"
with open("up.txt", "w") as file:
    file.write(text)
    print('\nFile closed?', file.closed)
print('File closed now?', file.closed)

with open("up.txt", "r+") as file:
    text = file.read()
    print('\nString', text)
    print('\nPos', file.tell())
    position = file.seek(10)
    print("Position in file", file.tell())

    file.write('All lands')

    file.seek(17)
    file.write('the min')

    file.seek(0)
    text = file.read()
print('\nString::', text)