"point stacker"
N = int(input())
point = 0
for _ in range(N):
    n = input()
    if n == "+":
        point += 10
    else:
        point -= 5
print(point)
