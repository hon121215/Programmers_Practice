def solution(myString, pat):
    answer = 0
    result = ''
    for x in myString:
        if x == 'A':
            result += 'B'
        else:
            result += 'A'
    answer = 1 if pat in result else 0
    return answer