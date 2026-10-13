"giraff"
N = int(input())
mylist = []
count = 0
for _ in range(N):
    mylist.append(int(input()))
for i in range(N):
    if N == 1:
        count = 1
    elif not i:
        if mylist[i] > mylist[i+1]:
            count += 1
    elif i == N-1:
        if mylist[i] > mylist[i-1]:
            count += 1
    else:
        if mylist[i-1]< mylist[i] > mylist[i+1]:
            count += 1
print(count)
