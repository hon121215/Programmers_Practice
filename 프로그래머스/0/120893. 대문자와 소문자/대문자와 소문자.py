def solution(my_string):
    answer = ''
    for x in my_string:
        answer += x.lower() if x < 'a' else x.upper()
    return answer