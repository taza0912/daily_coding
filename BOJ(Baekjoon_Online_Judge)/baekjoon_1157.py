S = list(input().upper())

S_doc = {}

for i in S:
    if i not in S_doc:
        S_doc[i] = 1
    else:
        S_doc[i] += 1

answer = ""

for i in S_doc.keys():
    if S_doc[i] == max(S_doc.values()):
        answer += i

if len(answer) == 1:
    print(answer)
else:
    print("?")