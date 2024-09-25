def solution(my_string, is_prefix):
    answer = 0
    string_list = []
    for x in range(len(my_string)):
        string_list.append(my_string[:-x])
    if is_prefix in string_list:
        answer += 1
    return answer