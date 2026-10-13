"Point Sorting"
def main():
    "Point Sorting"
    t = int(input())
    for _ in range(t):
        mylist = []
        n = int(input())
        for _ in range(n):
            x,y = map(int,input().split())
            mylist.append([x, y])
        mylist.sort(key=lambda x: (x[0] + x[1], -x[1]))
        for x,y in mylist:
            print(x, y)
main()
