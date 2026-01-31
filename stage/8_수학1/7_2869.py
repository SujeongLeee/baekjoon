a,b,v=map(int, input().split())
# tot = day = 0

# # first try
# while True:
#     tot += a
#     day += 1
#     # print(day)
#     if tot >= v:
#         print(day)
#         break
#     tot -= b

# 3 2 4
# 5-1+5

# 5 1 6
# 5-1+5

# 2 1 5
# 2-1+2-1+2-1+2

# 3 1 5
# 3-1+3

# 3 1 6
# 3-1+3-1+3-1

# 3 1 8
# 3-1+3-1+3-1+3-1

# 3 1 9
# 3-1+3-1+3-1+3-1+3

# 3 2 9
# 3-2+3-2+3-2+3-2+3-2+3-2+3-2+3

# daily_move = a-b

# # second try
# if dailymove==1:
#     print((v-a)//dailymove+1)
# elif v%dailymove==0:
#     print(v//dailymove)
# else:
#     print(v//dailymove+1)

# # third try
# until_last = v-a
# if until_last < a:
#     totdays = 2
# elif until_last == a:
#     totdays = v//daily_move
# else:
#     totdays = until_last//daily_move+1
# print(totdays)




days_before_last = (v - a + (a - b) - 1) // (a - b)
days_total = days_before_last + 1

days = (v - a + a - b - 1) // (a - b) + 1
print(days)