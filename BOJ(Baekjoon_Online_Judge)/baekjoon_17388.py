from sys import stdin

SKH = list(map(int, stdin.readline().split()))
u_doc = {SKH[0]: "Soongsil",
         SKH[1]: "Korea",
         SKH[2]: "Hanyang"}

if SKH[0] + SKH[1] + SKH[2] >= 100:
    print("OK")
else:
    print(u_doc[min(SKH)])
