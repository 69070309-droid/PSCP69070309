"plan plot"
L,N = map(int,input().split())
Line = 1
while (Line * L) * (Line * L + 1) // 2 < N:
    Line += 1
print(Line)
