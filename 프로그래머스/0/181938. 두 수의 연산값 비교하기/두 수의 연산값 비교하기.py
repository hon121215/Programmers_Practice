def solution(a, b):
    answer = 0
    ab = int(str(a) + str(b))
    ab2 = int(str(2*a*b))
    
    if ab >= ab2:
        return ab
    else:
        return ab2