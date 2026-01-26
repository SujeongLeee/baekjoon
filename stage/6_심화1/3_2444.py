# n = int(input())
# for i in range(1,n+1): # 1~5
#     spaces = " "*(n-i)
#     stars = '*'*(2*i-1)
#     print(spaces+stars+spaces) # 4~1로 다시 줄어들어야 함
# for i in range(n-1,0,-1):
#     spaces = " "*(n-i)
#     stars = '*'*(2*i-1)
#     print(spaces+stars+spaces)
# => 출력 형식이 잘못되었습니다 => 답에는 뒤에 공백이 없다고 함


# n = int(input())
# for i in range(1,n+1):
#     stars = "*"*(2*i-1)
#     print(stars.center(2*n-1)) # 문자열.center(전체길이, 채울문자)
# for i in range(n-1,0,-1):
#     stars = "*"*(2*i-1)
#     print(stars.center(2*n-1))
# => 출력 형식이 잘못되었습니다


# sol
n = int(input())
for i in range(1,n+1): # 1~5
    spaces = " "*(n-i)
    stars = '*'*(2*i-1)
    print(spaces+stars) # 4~1로 다시 줄어들어야 함
for i in range(n-1,0,-1):
    spaces = " "*(n-i)
    stars = '*'*(2*i-1)
    print(spaces+stars)
