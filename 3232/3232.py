"frog geppo"
a,b = map(int,input().split())
s = 0
count = 0
while s < b and a > 0:
    s += a
    count += 1
    a -= 2
if s >= b:
    print(count)
else:
    print("-1")
