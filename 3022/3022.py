"temperature cal"
temp = float(input())
tempin = input()
tempout = input()

if tempin == "F":
    temp = (temp - 32) * 5/9
elif tempin == "K":
    temp = temp - 273.15
elif tempin == "R":
    temp = (temp - 491.67) * 5/9
if tempout == "F":
    temp = (temp * 9/5) + 32
elif tempout == "K":
    temp = temp + 273.15
elif tempout == "R":
    temp = (temp * 9/5) + 491.67
print(f"{temp:.2f}")
