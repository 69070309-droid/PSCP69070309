"[LEARNING LOGS] Duplicate I"
def main():
    "[LEARNING LOGS] Duplicate I"
    m = int(input())
    n = int(input())
    groupm = set()
    groupn = set()
    for _ in range(m):
        x = int(input())
        groupm.add(x)
    for _ in range(n):
        f = int(input())
        groupn.add(f)
    dupe = groupm & groupn
    people = sorted(list(dupe),reverse=True)
    if people:
        print(*people, sep='\n')
    else:
        print("Nope")
main()
