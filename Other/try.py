day = 32
try:
    if day > 31:
        raise ValueError('Invalid Day Number')
except ValueError as er:
    print("Ошибка", er)
finally:
    print("All okey")