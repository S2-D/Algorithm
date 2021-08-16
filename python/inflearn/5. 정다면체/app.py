from os import supports_follow_symlinks
import sys

sys.stdin = open("inflearn/5. 정다면체/input.txt")

n, m = map(int, input().split())

cnt=[0]*(n+m+3)
max=0

for i in range(1,n+1):
  for j in range(1,m+1):
    cnt[i+j] +=1

for i in range(n+m+1):
  if cnt[i]>max:
    max=cnt[i]

for i in range(n+m+1):
  if cnt[i]==max:
    print(i, end=' ')

# 정 N면체, 정 M면체의 주사위 
# 두 개의 주사위 -> 눈의 합 중 가장 확률이 높은 숫자 출력. 
# 정답이 여러 개일 경우 : 오름차순 출력
# N과 M은 4,6,8,12,20 중 하나

