"[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"
def main():
    "[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"
    n,p = input().split()
    n = int(n)
    p = float(p)
    mylist = []
    totalblock = 0
    totalpoints = 0
    for _ in range(n):
        mylist.append(list(map(int,input().split())))
    for i in range(n):
        block = sum(1 for x in mylist[i] if x > 0)
        point = sum(mylist[i])
        totalblock += block
        totalpoints += point
        row = " ".join(map(str, mylist[i]))
        print(f"{row} {block} {point}")
    calblockl = []
    calpointl = []
    for j in range(n):
        calblock = sum(1 for i in range(n) if mylist[i][j] > 0)
        calpoint = sum(mylist[i][j] for i in range(n))
        calblockl.append(calblock)
        calpointl.append(calpoint)
    print(" ".join(map(str, calblockl)))
    print(" ".join(map(str, calpointl)))
    total_fine = totalpoints * p
    print(f"{totalblock} {totalpoints} {total_fine:.2f}")
main()
