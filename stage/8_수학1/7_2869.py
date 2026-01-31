a,b,v=map(int, input().split())
tot = day = 0

while True:
    tot += a
    day += 1
    # print(day)
    if tot >= v:
        print(day)
        break
    tot -= b