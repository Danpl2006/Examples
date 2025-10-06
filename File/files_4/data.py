import pickle, os

if not os.path.isfile('pickle.dat'):
    data = [0, 1]
    data[0] = input("Enter topic: ")
    data[1] = input("Enter series: ")
    file = open('pickle.dat', 'wb')
    pickle.dump(data, file)
    file.close()
else:
    file = open('pickle.dat', 'rb')
    data = pickle.load(file)
    file.close()
    print("WELCOME BACK  " +data[0] + ',' + data[1])