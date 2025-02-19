def solution(my_string):
    numarray = [str(x) for x in range(10)]
    output = ''
    result = 0
    for n in my_string:
        if n in numarray:
            output += n
        else:
            output += ' '

    num = [int(x) for x in output.split(' ') if x != '']
    return sum(num)