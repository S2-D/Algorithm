import sys

sys.stdin = open("input.txt")

T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s - 1 : e]
    a.sort()
    print(f"#{i+1} {a[k-1]}")
