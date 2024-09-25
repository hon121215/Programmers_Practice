def solution(n, control):
    for x in control:
        if x =='w':
            n += 1
        if x == 's':
            n -= 1
        if x == 'd':
            n += 10
        if x == 'a':
            n -= 10
            
    return n