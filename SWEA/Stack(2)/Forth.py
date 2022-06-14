Test_case = int(input())
for t in range(1, Test_case+1):
    cal = input().split()
    stack = []
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }
    for i in cal:
        if i == '.':
            if len(stack) > 1:
                result = "error"
            else:
                result = int(stack.pop())
        elif i in operators.keys():
            if len(stack) < 2:
                result = "error"
                break
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                c = operators[i](int(b), int(a))
                stack.append(int(c))
        else :
            stack.append(i)
    print("#{} {}".format(t, result))