"A-E-I-O-U"
text = input()
text = text.lower()
n = len(text)
a = 0
e = 0
i = 0
o = 0
u = 0
for x in range(n):
    if text[x] == "a":
        a += 1
    elif text[x] == "e":
        e += 1
    elif text[x] == "i":
        i += 1
    elif text[x] == "o":
        o += 1
    elif text[x] == "u":
        u += 1
if a:
    print("a :",a)
if e:
    print("e :",e)
if i:
    print("i :",i)
if o:
    print("o :",o)
if u:
    print("u :",u)
