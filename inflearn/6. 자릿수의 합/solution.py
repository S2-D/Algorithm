from os import supports_follow_symlinks
import sys

sys.stdin = open("/Users/damso/workspace/Algorithm_Python/inflearn/6. 자릿수의 합/input.txt")

n = int(input())
a = list(map(int, input().split()))

# 풀이 1 - digit_sum() : while문 사용 
# def digit_sum(x):
#   sum = 0
#   while x>0:
#     sum+= x%10
#     x=x//10
#   return sum

# max=-2147000000

# for x in a : 
#   tot=digit_sum(x)
#   if tot>max:
#     max=tot
#     res=x

# print(res)

############################

# 풀이 2 - digit_sum() : str으로 변환 
def digit_sum(x):
  sum = 0
  for i in str(x):
    sum+= int(i)
  return sum

max=-2147000000

for x in a : 
  tot=digit_sum(x)
  if tot>max:
    max=tot
    res=x

print(res)
