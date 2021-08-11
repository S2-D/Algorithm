def solution(scores):
    n = len(scores)
    newlist = []
    result = ""
    for i in range(n):
        newlist.append([])

    for i in range(n):
        for j in range(n):
            newlist[j].append(scores[i][j])

    for i in range(n):
        sum = 0
        cnt = 0
        for j in range(n):
            if not (
                (
                    (i == j)
                    and (max(newlist[i]) == newlist[i][i])
                    and (newlist[i].count(max(newlist[i])) == 1)
                )
                or (
                    (i == j)
                    and (min(newlist[i]) == newlist[i][i])
                    and (newlist[i].count(min(newlist[i])) == 1)
                )
            ):
                sum += newlist[i][j]
                cnt += 1
        avg = sum / cnt
        if avg >= 90:
            result += "A"
        elif avg >= 80:
            result += "B"
        elif avg >= 70:
            result += "C"
        elif avg >= 50:
            result += "D"
        else:
            result += "F"
    return result


print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
