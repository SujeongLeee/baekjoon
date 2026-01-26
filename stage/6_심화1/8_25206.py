scores = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0
}

result = 0
tot_time = 0

for i in range(20):
    name, time, grade = input().split()

    if grade=='P':
        continue # 밑에 계산하지 않고 다음 i로 넘어감
    
    score = scores[grade]
    fscore = float(score)

    ftime = float(time)
    tot_time += ftime
    
    result += ftime*fscore

print(result/tot_time)
