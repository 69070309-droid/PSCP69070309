"Arcade of Time: Store Check"
num, check = map(int, input().split())

checklist = []

for _ in range(num):
    time1, time2 = map(int, input().split())
    checklist.append((time1, time2))

timetogo = list(map(int, input().split()))

result = []

for i in range(check):
    time = timetogo[i]
    count = 0

    for time1, time2 in checklist:
        if time1 <= time < time2:
            count += 1

    result.append(str(count))

print(" ".join(result))
