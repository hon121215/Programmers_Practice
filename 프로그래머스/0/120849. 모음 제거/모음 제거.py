def solution(my_string):
    vowel = ['a','e','i','o','u']
    for x in vowel:
        my_string = my_string.replace(x,'')
    return my_string