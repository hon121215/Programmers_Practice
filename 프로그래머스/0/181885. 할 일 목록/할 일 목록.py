def solution(todo_list, finished):
    answer = []
    for x in range(len(todo_list)):
        if finished[x] == False:
            answer.append(todo_list[x])
    return answer