# # sol1
# # 리스트[a:b] -> a 이상 b 미만
# # 조잡....
# s = input()
# slist = list(s)
# slen = len(slist)
# # print(slist); print(slen)
# if slen%2==0:
#     idx = int(slen/2)
#     left = slist[0:idx]
#     right = slist[idx:slen][::-1]
#     # print(left); print(right)
#     if left==right:
#         print(1)
#     else:
#         print(0)
# else:
#     idx = int((slen-1)/2)
#     left = slist[0:idx]
#     right = slist[idx+1:slen][::-1]
#     # print(left); print(right)
#     if left==right:
#         print(1)
#     else:
#         print(0)

# GPT
s = input().strip()
print(1 if s == s[::-1] else 0)