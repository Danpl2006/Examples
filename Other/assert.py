# Нахождение ошибки
chars = ["Alpha", "Beta", "Gamma"]
def disp(elem):
    assert type(elem) is int, "argument must be int!"
    print("List elem", elem, "=", chars[elem])
elem = None
disp(elem)