X = int(input())

i = 1
while i <= X:
    if (i*i - i + 2)/2 <= X:
        i += 1
    else:
        i -= 1
        break
s = X - int((i*i - i + 2)/2)

print(i, s)

if X == 1:
    print("1/1")
elif X == 2:
    print("1/2")
else:
    if i%2 == 1:
        print(str(i-s)+"/"+str(1+s))
    else:
        print(str(1+s)+"/"+str(i-s))