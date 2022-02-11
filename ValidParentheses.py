# Given a string s containing just the characters '(', ')', '{','}', '[',']'
# determine if the input string is valid
# an input string is valid if:
    # 1. open brackets must be closed by the same type of brackets.
    # 2. open brackets must be closed in the correct order.

# input: s = '()'
# output: true

# input: s = '()[]{}'
# output: true

# cheet = {"(":")", "{": "}", "[": "]"}
# cheet = {")": "(", "}" : "{", "]" : "["}
#print(cheet['('])

s = "()"
def isValid(s):
    cheet = {"(":")", "{": "}", "[": "]", ")": "(", "}": "{", "]": "["}

    for idx in range(len(s)-1):
        target = s[idx]
        if idx==0 and (target==")" or target=="}" or target=="]"):
            return False
        if cheet[target] == s[idx+1]:
            continue
        elif cheet[target] == s[idx-1]:
            continue
        else:
            return False
    return True
print(isValid(s))
