"[LEARNING LOGS] CuteCat CuteFox"
def main():
    "[LEARNING LOGS] CuteCat CuteFox"
    cat = 0
    fox = 0
    mycat = {}
    myfox = {}
    N = int(input())
    for _ in range(N):
        key, value = input().split(":")
        if value[2:5] == "Cat":
            cat += 1
            mycat.update({key.strip('{} "'): value.strip('{} "')})
        elif value[2:5] == "Fox":
            fox += 1
            myfox.update({key.strip('{} "'): value.strip('{} "')})
    mycat = dict(sorted(mycat.items(), key=lambda x: x[1]))
    myfox = dict(sorted(myfox.items(), key=lambda x: x[1]))
    if "Cat01" not in mycat.values() and "Garfield" not in mycat.keys():
        if "Garfield" not in myfox.keys():
            mycat.update({"Garfield": "Cat01"})
            cat += 1
    if "Fox01" not in myfox.values() and "Fubuki" not in myfox.keys():
        if "Fubuki" not in mycat.keys():
            myfox.update({"Fubuki": "Fox01"})
            fox += 1
    mycat = dict(sorted(mycat.items(), key=lambda x: int(x[1][3:])))
    myfox = dict(sorted(myfox.items(), key=lambda x: int(x[1][3:])))
    print(f"Cat : {cat}")
    print(f"Fox : {fox}")
    for i in mycat:
        print(f"{i} : {mycat[i]}")
    for i in myfox:
        print(f"{i} : {myfox[i]}")
main()
