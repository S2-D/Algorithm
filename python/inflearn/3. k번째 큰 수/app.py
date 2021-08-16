import sys

sys.stdin = open("input.txt")

n, K = map(int, input().split())
a = list(map(int, input().split()))

result = []

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if a[i]+a[j]+a[k] not in b:
        result.append(a[i]+a[j]+a[k])

result.sort()
print(result[-K])


# 1 <= N <= 100 
# N장의 카드 중 3장 뽑아 각 카드에 적힌 수 합한 값 기록 
# 모든 경우의 수 중 k번째 큰 수 출력하기 
# a = N개의 카드값


# 중복값이 필요 없으므로 set을 활용해도 좋을 것. 