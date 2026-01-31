import cgi

data = cgi.FieldStorage()

answer = data.getvalue('cat')
if answer == 'Marlup':
    result = answer + 'Is correct'
else:
    result = answer + 'is incorrect'

print("Content-type: text/html\r\n\r\n")
print('''<!DOCTYPE HTML>''')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Python Response cars</title>')
print('</head>')
print('<body>')
print( '<h1>', result , '</h1>')
print('<a href="radio.html">Back</a>')
print('</body>')
print('</html>')