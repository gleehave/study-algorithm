T = int(input())

for _ in range(T):
    Data = input()
    list_data = list(Data)
    count = 0

    for i in list_data:
        if i == "(":
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            print('NO')
            break
    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')