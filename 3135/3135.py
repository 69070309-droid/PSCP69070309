"asd"
def main():
    "gift"
    N, K, T = map(int, input().split())
    p = 1
    visited = {1}
    while p != T:
        p = (p + K - 1) % N + 1

        visited.add(p)

        if p == 1:
            break
    print(len(visited))
main()
