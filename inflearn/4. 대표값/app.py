import sys

sys.stdin = open("Algorithm_Python/inflearn/4. 대표값/input.txt")

n = int(input())
scores = list(map(int, input().split()))

ave = round(sum(scores)/n)

a = []

for i, score in enumerate(scores):
  new_var = score - ave
  if a == [] or abs(a[-1][1]) > abs(new_var) :
    a.append([i, new_var])
  elif (abs(a[-1][1]) == abs(new_var)) and (new_var >=0) and (a[-1][1] != new_var):
    a.append([i, new_var])

print(ave, a[-1][0]+1)

# n = 학생 수 
# scores = 학생들의 수학 점수
# 평균을 구하고 평균에 가장 가까운 학생이 몇 번째인지 출력
# 여러 개일 경우 우선 순위 : 점수가 높은 학생 번호 / 학생 번호가 빠른 순 
# 평균은 소수 첫째 자리에서 반올림