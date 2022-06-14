# # 괄호 {} () 가 제대로 짝을 이뤘는지 검사한다.
# # good: {()} -> 1
# # bad: {(})  -> 0
#
# def check(stack):
#     N = len(stack)
#     temp = []
#     while N > 0:
#         print("stack: ", stack)
#         print("temp: ", temp)
#         ready = stack.pop(0)
#         N -= 1
#
#         if ready in cheat.keys():
#             temp.append(ready)
#             continue
#         if ready in cheat.values():
#             compare = temp.pop()
#             if cheat[compare] == ready:
#                 continue
#             else:
#                 return 0
#     if temp:
#         return 0
#     else:
#         return 1
#
# T = int(input())
# for test_case in range(1, T + 1):
#     data = input()
#     stack = []
#     cheat = {
#         '{': '}',
#         '(': ')',
#     }
#     for value in data:
#         if (value in cheat.keys()) or (value in cheat.values()):
#             stack.append(value)
#
#     result = check(stack)
#     print("#{} {}".format(test_case, result))

Test_case = int(input())

for t in range(1, Test_case+1):
    stack = []
    ans = 1
    string = str(input())
    arr = list(string)
    for i in range(0, len(arr)):
        if arr[i] == '(' or arr[i]=='{':
            stack.append(arr[i])
        elif arr[i] == ')' or arr[i]=='}':
            if not stack:
                ans=0
                break
            P = stack.pop()
            if arr[i] == ')' and P!='(':
                ans = 0
            elif arr[i] == '}' and P != '{':
                ans = 0
    if stack:
        ans = 0
    print("#{} {}".format(t,ans))