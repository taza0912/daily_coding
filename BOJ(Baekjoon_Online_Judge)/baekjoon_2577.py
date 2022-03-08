import sys

nums = [int(sys.stdin.readline()) for _ in range(3)]

ABC = nums[0] * nums[1] * nums[2]

counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in str(ABC):
    counts[int(i)] += 1

for j in range(10):
    print(counts[j])