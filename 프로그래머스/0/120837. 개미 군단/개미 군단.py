def solution(hp):
    answer = 0
    if hp >= 5:
        answer += hp // 5
        hp = hp%5
        answer += hp // 3
        hp = hp%3
        answer += hp
    elif hp >= 3:
        answer += hp // 3
        hp = hp%3
        answer += hp
    elif hp >= 1:
        answer += hp
    
    return answer