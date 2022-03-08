from sys import stdin

t = int(stdin.readline())
for i in range(t):
    val = int(stdin.readline())
    print(val//25, (val%25)//10, ((val%25)%10)//5, ((val%25)%10)%5)