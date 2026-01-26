num = [1,1,2,2,2,8]
# s = input()
# print([num[i]-int(s[i]) for i in range(len(num))]) # 이렇게 하면 s에 공백이 있을 수 있으므로 안됨
s = list(map(int, input().split())) # 각각을 숫자로 받아야 함
# print(num-s) #  이렇게는 안됨
result = [num[i]-s[i] for i in range(len(num))]
print(*result)
