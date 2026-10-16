"padthai"
def main():
    "padthai"
    fullcourse = {"Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp",
"Bean Sprouts","Noodle","Chives","Lime","Egg","Oil","Peanuts"}
    delirious = {"Sweet","Sour","Salty"}
    nutrient = set()
    tasty = set()
    while True:
        material = input()
        if material == "Cook":
            break
        nutrient.add(material)
    while True:
        tast = input()
        if tast == "End":
            break
        tasty.add(tast)
    if not nutrient.issubset(fullcourse):
        print("This is not Pad Thai!!!")
    elif nutrient != fullcourse:
        print("This is bad!")
    else:
        if tasty == delirious:
            print("Delicious!")
        else:
            print("Not Bad...")
main()
