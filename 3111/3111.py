"สหกรณ์โรงงาน"
import math
def round_half(n,decimals=0):
    "round_half function"
    multiple = 10**decimals
    adjusted = (n * multiple)+ 1e-9
    if adjusted >= 0:
        result = math.floor(adjusted + 0.5)
    else:
        result = math.ceil(adjusted - 0.5)
    return result / multiple
a = input()
b = int(input())
amount = 0
for i in range(b):
    i = i + 1
    x = float(input())
    amount += x
if a == "Y":
    amount = amount*0.95
elif a == "N":
    if amount >= 500:
        amount = amount * 0.97
amount = round_half(amount,2)
print(f'{amount:.2f}')
