import sys

sys.stdin = open("input.txt")

n, k = map(int, input().split())

divisors = []

for i in range(n):
    if n % (i + 1) == 0:
        divisors.append(i + 1)


if len(divisors) < (k - 1):
    print(-1)
else:
    print(divisors[k - 1])
