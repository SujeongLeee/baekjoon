# t = int(input())
# for _ in range(t):
#     c = int(input())/100 # 달러
#     # quarter 0.25
#     nq = c//0.25
#     # dime 0.1
#     nd = (c%0.25)//0.1
#     # nickel 0.05
#     nn = ((c%0.25)%0.1)//0.05
#     # penny 0.01
#     if (((c%0.25)%0.1)%0.05)%0.01==0:
#         np = (((c%0.25)%0.1)%0.05)//0.01
#     else:
#         np = (((c%0.25)%0.1)%0.05)//0.01+1
#     print(int(nq), int(nd), int(nn), int(np))

# 위에처럼 하면 float 특성상 에러 뜰 수 있다고 함
t = int(input())
for _ in range(t):
    c = int(input()) # 달러
    # quarter 0.25
    nq = c//25
    # dime 0.1
    nd = (c%25)//10
    # nickel 0.05
    nn = ((c%25)%10)//5
    # penny 0.01
    if (((c%25)%10)%5)%1==0:
        np = (((c%25)%10)%5)//1
    else:
        np = (((c%25)%10)%5)//1+1
    print(int(nq), int(nd), int(nn), int(np))