t = int(input())

for _ in range(t):
    R, S = input().split()
    R = int(R)

    new_S = str()

    for char in S:
        new_S += char * R
    
    print(new_S)