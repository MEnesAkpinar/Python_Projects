"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


"""

def isValid(s):
    stack = []
    symbols = {")" : "(",
               "}" : "{",
               "]" : "["}
    for char in s:
        if char in symbols.values():
            stack.append(char)
        elif char in symbols.keys():
            if stack and stack[-1] == symbols[char]:
                stack.pop()
            else:
                return False
            
    return not stack 