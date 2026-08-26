"asd"
A = int(input())
B = int(input())
goal = int(input())
if (5*B)+A >= goal:
    if goal//5 <= B:
        goal = goal-((goal//5)*5)
        if goal > A:
            print("-1")
        else:
            print(goal)
    elif goal//5 > B:
        goal = goal -(B*5)
        print(goal)
else:
    print("-1")
