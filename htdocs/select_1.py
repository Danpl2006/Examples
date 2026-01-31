import cgi

data = cgi.FieldStorage()

city = data.getvalue('Citylist')


print("Content-type: text/html\r\n\r\n")
print('''<!DOCTYPE HTML>''')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Python Response cars</title>')
print('</head>')
print('<body>')
print( '<h1>City:', city , '</h1>')
print('<a href="select.html">Back</a>')
print('</body>')
print('</html>')