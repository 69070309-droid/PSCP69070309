"[LEARNING LOGS] Shorten"
def main():
    "[LEARNING LOGS] Shorten"
    mylist = []
    ans = []
    x = int(input())
    if x != -1:
        mylist.append([x,-67])
        while True:
            x = int(input())
            if x == -1:
                break
            if x in (mylist[-1][0] + 1, mylist[-1][1] + 1):
                mylist[-1][1] = x
            else:
                mylist.append([x,-67])
        for i in mylist:
            if i[1] == -67:
                ans.append(str(i[0]))
            else:
                ans.append(f'{i[0]}-{i[1]}')
        print(", ".join(ans))
main()
