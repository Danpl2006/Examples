import cgi

data = cgi.FieldStorage()

make = data.getvalue('make')
model = data.getvalue('model')

print("Content-type: text/html\r\n\r\n")
print('''<!DOCTYPE HTML>''')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Python Response cars</title>')
print('</head>')
print('<body>')
print( '<h1>', make, model , '</h1>')
print('<a href="post.html">Back</a>')
print('</body>')
print('</html>')