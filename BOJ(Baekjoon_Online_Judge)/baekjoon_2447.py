from sys import stdin


# i, j in range(int(n/3)+1, int((n*2)/3)+1)
def star(n):
    if n == 3:
        for i in range(1, n+1):
            for j in range(1, n+1):
                if j in range(int(n/3)+1, int((n*2)/3)+1):
                    if i in range(int(n/3)+1, int((n*2)/3)+1):
                        print(" ", end="")
                    else:
                        print("*", end="")
                else:
                    print("*", end="")
            print()
        return star(n)
    else:
        return star(star(n/3))

N = int(stdin.readline())

star(N)