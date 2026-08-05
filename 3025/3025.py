"Season"
month = int(input(""))
date = int(input(""))
if month in (1,2):
    print("winter")
elif month == 3:
    if date < 21:
        print("winter")
    else:
        print("spring")
elif month in (4,5):
    print("spring")
elif month == 6:
    if date < 21:
        print("spring")
    else:
        print("summer")
elif month in (7,8):
    print("summer")
elif month == 9:
    if date < 21:
        print("summer")
    else:
        print("fall")
elif month in (10,11):
    print("fall")
elif month == 12:
    if date < 21:
        print("fall")
    else:
        print("winter")
