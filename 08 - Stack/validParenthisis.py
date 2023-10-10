def isValidParenthesis(s):
    stack = []

    bracketMapping = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for i in s:
        if i in bracketMapping.values():
            stack.append(i)

        elif i in bracketMapping.keys():
            if not stack or stack.pop()!=bracketMapping[i]:
                return False
            
    return True


print(isValidParenthesis("(([]))"))
print(isValidParenthesis( "({[})"))
# print(isValidParenthesis(""))
# print(isValidParenthesis(""))
# print(isValidParenthesis(""))
# print(isValidParenthesis(""))
# print(isValidParenthesis(""))
# print(isValidParenthesis(""))
# print(isValidParenthesis(""))



