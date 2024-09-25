def solution(my_string):
    answer = 0
    num = [str(x+1) for x in range(9)]
    hide = [int(x) for x in my_string if x in num]
    
    return sum(hide)