def solution(n):
    answer = []
    while True:
        answer.append(n)
        if n%2 == 0:
            n = n/2
            if n == 2:
                answer.append(n)
                n = n/2
                answer.append(n)
                break
        else:
            n = 3*n+1
    return answer