"lottory"
cost = 0
text = input()
textbuy = input()
if text == textbuy:
    cost = 1000000
elif text[2:] == textbuy[2:]:
    cost = 100000
elif text[4:] == textbuy[4:] and text[0] == textbuy[0]:
    cost = 2000
elif text[5:] == textbuy[5:] and text[0] == textbuy[0]:
    cost = 1000
elif text[4:] == textbuy[4:]:
    cost = 200
elif text[5:] == textbuy[5:]:
    cost = 100
elif text[0] == textbuy[0]:
    cost = 20
else:
    cost = 0
print(cost)
