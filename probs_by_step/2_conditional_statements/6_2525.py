start_h, start_m = map(int, input().split())
time = int(input())

finish_m = start_m + time
finish_h = start_h + finish_m // 60
finish_h %= 24
finish_m %= 60

print(finish_h, finish_m)