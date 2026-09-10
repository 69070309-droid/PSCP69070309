"สงคราม...ส่งด่วน"
a = input()
b = float(input())
amount = 0
if a == "BKK CNX":
    amount += 10
    amount += b * 30
    print(f'{amount:.2f}')
elif a == "CNX UBP":
    amount += 15
    amount += b * 40
    print(f'{amount:.2f}')
elif a == "UBP BKK":
    amount += 20
    amount += b * 40
    print(f'{amount:.2f}')
elif a == "BKK PKT":
    amount += 25
    amount += b * 50
    print(f'{amount:.2f}')
elif a == "PKT CNX":
    amount += 30
    amount += b * 60
    print(f'{amount:.2f}')
elif a == "UBP PKT":
    amount += 40
    amount += b * 70
    print(f'{amount:.2f}')
else:
    print("Error")
