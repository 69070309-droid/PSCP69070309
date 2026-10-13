"[LEARNING LOGS] หั่นขนมปัง"
def main():
    "[LEARNING LOGS] หั่นขนมปัง"
    w, h, m, n = map(int, input().split())
    m += 1
    n += 1
    wide = [0]
    max_wide = []
    length = [0]
    max_length = []
    ans = []
    second_max = []

    wide.extend(map(int, input().split()))

    for i in range(1, len(wide)):
        max_wide.append(wide[i] - wide[i-1])
    max_wide.append(w - wide[-1])
    max_wide.sort(reverse=True)

    length.extend(map(int, input().split()))
    for i in range(1, len(length)):
        max_length.append(length[i] - length[i-1])
    max_length.append(h - length[-1])
    max_length.sort(reverse=True)


    ans.append(max_wide[0] * max_length[0])
    if len(max_wide) > 1:
        second_max.append(max_wide[1] * max_length[0])
    if len(max_length) > 1:
        second_max.append(max_wide[0] * max_length[1])

    if second_max:
        ans.append(max(second_max))
    else:
        ans.append(ans[0])

    print(" ".join(map(str, ans)))

main()
