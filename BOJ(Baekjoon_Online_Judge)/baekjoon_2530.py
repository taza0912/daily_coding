from sys import stdin
import datetime

A, B, C = map(int, stdin.readline().split())
current_time = datetime.timedelta(hours=A, minutes=B, seconds=C)
current_time += datetime.timedelta(seconds=int(input()))

print(int(str(current_time)[-8:-6]), int(str(current_time)[-5:-3]), int(str(current_time)[-2:]))