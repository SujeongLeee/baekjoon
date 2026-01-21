# 평균
n = int(input())
s1,s2,s3 = map(int, input().split())

m = max(s1,s2,s3)
s1new = s1/m*100
s2new = s2/m*100
s3new = s3/m*100

print((s1new+s2new+s3new)/3)