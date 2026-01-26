n = int(input())
for i in range(1,n+1): # 1~5
    spaces = " "*(n-i)
    stars = '*'*(2*i-1)
    print(spaces+stars+spaces) # 4~1로 다시 줄어들어야 함
for i in range(n-1,0,-1):
    spaces = " "*(n-i)
    stars = '*'*(2*i-1)
    print(spaces+stars+spaces)