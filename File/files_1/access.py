file = open('example.txt', 'w')
print("Name > ", file.name)
print("Mode > ", file.mode)
print("R > ", file.readable())
print("W > ", file.writable())

def get_stat(f):
    if f.closed :
        return "Closed"
    else:
        return "Open"
print("File Status: ", get_stat(file))
file.close()
print("Status", get_stat(file))
