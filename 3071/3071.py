"r&d"
A = int(input())
B = int(input())
d = int(input())
r = int(input())
N = 0

while A <= B:
    if A % d == r:
        N += 1
    A += 1
print(N)
