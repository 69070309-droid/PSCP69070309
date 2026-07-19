"color mixing"
COLOR1 = str(input(""))
COLOR2 = str(input(""))
if COLOR1 != COLOR2:
    if COLOR1 == "Red" or COLOR2 == "Red":
        if COLOR2 == "Yellow" or COLOR1 == "Yellow":
            print("Orange")
        elif COLOR2 == "Blue" or COLOR1 == "Blue":
            print("Violet")
        else:
            print("Error")
    elif COLOR1 == "Blue" or COLOR2 == "Blue":
        if COLOR2 == "Yellow" or COLOR1 == "Yellow":
            print("Green")
        else:
            print("Error")
    else:
        print("Error")
elif COLOR1 == COLOR2:
    if COLOR1 == "Red":
        print("Red")
    elif COLOR1 == "Blue":
        print("Blue")
    elif COLOR1 == "Yellow":
        print("Yellow")
    else:
        print("Error")
