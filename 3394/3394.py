"[LEARNING LOGS] ส่งต่อ"
def main():
    "[LEARNING LOGS] ส่งต่อ"
    n, s = map(int, input().split())
    nextper = [0] * (n + 1)
    for i in range(1, n + 1):
        nextper[i] = int(input())
    visited = set()
    current = s
    while current and current not in visited:
        visited.add(current)
        current = nextper[current]
    print(len(visited))
main()
