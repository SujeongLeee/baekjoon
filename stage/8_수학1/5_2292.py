# 벌집
n = int(input())
# 1: 1개 = 6 * (shell - 1)
# 2~7: 6개 = 6*1 = 6 * (shell - 1)
# 8~19: 12개 = 6*2
# 20~37: 18개 = 6*3
# 38~61: 24개 = 6*4
# ...

# rowlen=[1]
# for i in range(1,n):
#     rowlen.append(6*i)
# # print(rowlen)

# firstval=[]
# for i in range(1,n):
#     firstval.append(sum(rowlen[:i-1])+1) # 전체 리스트에 각각 1씩 더하고 싶음
# # print(firstval)

# for i in range(n):
#     if n < firstval[i]:
#         here = i
#         print(i)
#         exit() # 처음 나오면 프린트하고 종료
# print(here)


n = int(input())
if n == 1:
    print(1)
else:
    n -= 1
    shell = 2
    
    while True:
        n -= 6 * (shell - 1)
        if n <= 0:
            print(shell)
            break
        shell += 1