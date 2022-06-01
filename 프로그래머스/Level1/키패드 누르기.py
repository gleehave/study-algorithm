def calculateDistance(handnumber, nextnumber):
    keypad = {
        1:[0,0], 2:[1,0], 3:[2,0],
        4:[0,1], 5:[1,1], 6:[2,1],
        7:[0,2], 8:[1,2], 9:[2,2],
        '*':[0,3], 0:[1,3], '#':[2,3]
    }

    x1, y1 = keypad[handnumber]
    x2, y2 = keypad[nextnumber]
    return abs(x1-x2) + abs(y1-y2)

def solution(numbers, hand):
    answer = ''
    leftLocation = "*"
    rightLocation = "#"

    fix_thumb = {
        1: 'L',
        4: 'L',
        7: 'L',
        3: 'R',
        6: 'R',
        9: 'R',
    }

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            leftLocation = number
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            rightLocation = number
        elif number == 2 or number == 5 or number == 8 or number == 0:
            leftDistance = calculateDistance(leftLocation, number)
            rightDistance = calculateDistance(rightLocation, number)

            if leftDistance < rightDistance:
                answer += 'L'
                leftLocation = number
            elif rightDistance < leftDistance:
                answer += 'R'
                rightLocation = number
            else:
                if hand == 'left':
                    answer += 'L'
                    leftLocation = number
                else:
                    answer += 'R'
                    rightLocation = number
    return answer