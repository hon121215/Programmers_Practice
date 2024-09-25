def solution(my_string, is_suffix):
    answer = 0
    word_list = []
    for x in range(len(my_string)):
        word_list.append(my_string[-x:])
    for y in word_list:
        if y==is_suffix:
            answer += 1
    return answer