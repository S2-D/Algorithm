def solution(price, money, count):
    total = 0

    for i in range(1, count + 1):
        total += price * i

    if total > money:
        return total - money
    else:
        return 0


# 문제 : https://programmers.co.kr/learn/courses/30/lessons/82612
