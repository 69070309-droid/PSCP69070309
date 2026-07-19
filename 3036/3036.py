"cal pyramid"
SN = int(input())
mylist = []
i = 1
floor = 0

while sum(mylist) < SN:
    mylist.append(i)
    i += 2
    floor += 1
mylist.sort(reverse=True)
if SN > 1 :
    if not floor % 2:
        if not SN % 2:
            ANSWER = mylist[0] - 1
        else:
            ANSWER = mylist[0] - 2
    else:
        if not SN % 2:
            ANSWER = mylist[0] - 2
        else:
            ANSWER = mylist[0] - 1
else:
    ANSWER = 0
print(ANSWER)
