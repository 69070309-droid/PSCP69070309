"card 44"
score = ""
card = ""
Totalcard = ""
text = input().upper()
if text[-1] == "D":
    card = "diamonds"
elif text[-1] == "H":
    card = "hearts"
elif text[-1] == "S":
    card = "spades"
elif text[-1] == "C":
    card = "clubs"
if len(text) == 2:
    if text[0].isdigit():
        score = text[0]
    else:
        if text[0] == "A":
            score = "ace"
        elif text[0] == "J":
            score = "jack"
        elif text[0] == "Q":
            score = "queen"
        elif text[0] == "K":
            score = "king"
else:
    score = text[:2]
Totalcard = score+" of "+card
print(Totalcard)
