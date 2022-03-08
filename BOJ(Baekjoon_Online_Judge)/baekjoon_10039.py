Total_Score = 0
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    Total_Score += score

print(int(Total_Score/5))