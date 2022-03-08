val = input()
if len(val) == 2:
    print(int(val[0]) + int(val[1]))
elif len(val) == 4:
    print(20)
elif val.index("0") == 1:
    print(10 + int(val[-1]))
else:
    print(10 + int(val[0]))