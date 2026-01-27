# n = int(input())
# mat = [[0]*100 for _ in range(100)]
# for _ in range(n):
#     x,y = map(int, input().split())
#     for i in range(((100-y)-9-1),(100-y)):
#         for j in range((x-1),((x-1)+9+1)):
#             mat[i][j]=1  
# print(sum(row.count(1) for row in mat))




# 도형 뒤집으면 똑같으니까
n = int(input())
mat = [[0]*100 for _ in range(100)]
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            mat[i][j]=1  
print(sum(row.count(1) for row in mat))





# # 첫번째 시도
# n = int(input())
# pair = []

# for _ in range(n):
#     ldist, bdist = map(int, input().split())
#     pair.append([ldist, bdist])

# overlap = 0
# for i in range(n-1):
#     for j in range(1,n-i):
#         l = abs(pair[i][0]-pair[i+j][0])
#         r = abs(pair[i][1]-pair[i+j][1])
#         if l>= 10 or r >= 10: 
#             overlap += 0
#         else:
#             ll = abs(pair[i][0]+10 - pair[i+j][0])
#             rr = abs(pair[i+j][1]+10 - pair[i][1])
#             overlap += ll*rr

# # print(overlap)
# print((10**2)*3-overlap)

# # 어떤 영역이 여러번 겹치는 경우에는 ??????? 불가능 !!!



