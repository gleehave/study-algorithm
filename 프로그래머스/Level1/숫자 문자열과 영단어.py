def solution(s):
    sheet = {
        'zero' : '0',
        'one'  : '1',
        'two'  : '2',
        'three': '3',
        'four' : '4',
        'five' : '5',
        'six'  : '6',
        'seven': '7',
        'eight': '8',
        'nine' : '9'
    }
    result = ''
    char = ''
    for value in s:
        if value.isdigit():
            result += value
        elif value.isalpha():
            char += value
            if char in sheet.keys():
                result += sheet[char]
                char = ''

    return int(result)