s = "Что-то"
print("Red string: ", s)
print("Type", type(s), "Len", len(s))

s = s.encode("utf-8")
print("Encoded >", s)
print("Type", type(s), "Len", len(s))

s = s.decode("utf-8")
print("Decoded >", s)
print("Type", type(s), "Len", len(s))

import unicodedata
for i in range(len(s)):
    print(s[i], unicodedata.name(s[i]), sep=":")

s = b'Gr\xc3\xb6n'
print("Green > ", s.decode('utf-8'))

s = "Gr\N{CYRILLIC SMALL LETTER TE}n"
print("Green 2", s)