ndoc = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
}

nstr = input()[::-1]

answer = 0
for i in range(len(nstr)):
    answer += ndoc[nstr[i]]*(16**i)

print(answer)