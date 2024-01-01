from sys import stdin

N = int(stdin.readline())

n_doc = {}
for i in range(N):
    val = input()
    if len(val) not in n_doc:
        n_doc[len(val)] = [val]
    elif val not in n_doc[len(val)]:
        n_doc[len(val)].append(val)
    else:
        pass

for j in sorted(n_doc):
    for k in sorted(n_doc[j]):
        print(k)


# from sys import stdin

# N = int(stdin.readline())
# n_doc = {}
# for i in range(N):
#     val = str(stdin.readline())[:-1]
#     if len(val) not in n_doc:
#         n_doc[len(val)] = [val]
#     elif val not in n_doc[len(val)]:
#         n_doc[len(val)].append(val)

# for j in sorted(n_doc.keys()):
#     temp = len(n_doc[j])
#     for k in range(temp):
#         print(sorted(n_doc[j])[k])
    