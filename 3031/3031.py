"INK"
import math
INK_PEOPLE = input()
PEOPLE_split = INK_PEOPLE.split(" ")
PI = 3.1416
for i in range (int(PEOPLE_split[1])):
    i = i+1
    tumneung = input()
    tumneung_split = tumneung.split(" ")
    distant = (int(tumneung_split[0])**2)+(int(tumneung_split[1])**2)
    print(math.ceil((PI*distant)/int(PEOPLE_split[0])))
