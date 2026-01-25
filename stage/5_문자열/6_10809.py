# sol1
# S = str(input())
# for i in range(ord('a'), ord('z')+1):
#     where = S.find(chr(i))
#     if i==ord('z'):
#         print(where)
#     else:
#         print(where, end=" ")

# sol2
S = str(input())
s = ""
for i in range(ord('a'), ord('z')+1):
    s += str(S.find(chr(i))) + " "
print(s.rstrip())

# sol3
# S = str(input())
# s = str(S.find(chr(ord('a'))))
# for i in range(ord('a')+1, ord('z')+1):
#     s += " " + str(S.find(chr(i)))
# print(s)