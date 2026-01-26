made = []
lens = []
for _ in range(5):
    s = list(input())
    made.append(s)
    lens.append(len(s))

maxlen = max(lens)

for j in range(maxlen):
    for i in range(5):
        if j < len(made[i]): # j는 최대 maxlen-1
            read = made[i][j]
        else:
            read=''
        print(read, end='')     
