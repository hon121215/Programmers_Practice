def solution(box, n):
    answer = 1
    dice = [x//n for x in box]
    for x in dice:
        answer *= x
    return answer