from os import supports_follow_symlinks
import sys

sys.stdin = open("/Users/damso/workspace/Algorithm_Python/inflearn/6. 자릿수의 합/input.txt")

n = int(input())
a = list(map(int, input().split()))

max = 0
max_index = 0

def digit_sum(x):
  if x < 10:
    return x % 10
  else:
    return x % 10 + digit_sum(x//10)


for i, num in enumerate(a):
  if max < digit_sum(num):
    max = digit_sum(num)
    max_index = i

print(a[max_index])

# 각 자리수의 합이 최대인 자연수를 출력
# 자릿수 합을 구하는 함수는 digit_sum(x) 만들어 사용할 것
# 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자 출력  
