"Vat&Service price"

price = float(input(""))
if price*0.1 <= 50:
    SERVICE = 50
elif price*0.1 >= 1000:
    SERVICE = 1000
else:
    SERVICE = price*0.1
vat = (price+SERVICE)*0.07
total_price = price + SERVICE + vat
print(f"{total_price:.2f}")
