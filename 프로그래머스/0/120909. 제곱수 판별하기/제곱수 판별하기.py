def solution(n):
    for x in range(1,n):
        if x**2 == n:
            result = 1
            break
        else:
            result = 2
    return result