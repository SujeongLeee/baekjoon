# EOF: End of File: 입력이 끝났다는 신호
# 입력이 몇줄인지 안알려주고 입력이 끝날때까지 받아야 함.
while True:
    try:
        print(input())
    except EOFError:
        break