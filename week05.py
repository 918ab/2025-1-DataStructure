def check_parentheses(expression : str) -> bool:
    stack = []
    for latter in expression:
        if latter == "(":
            stack.append(latter)
        if latter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return  len(stack) == 0


print(check_parentheses("(2+3)"))
print(check_parentheses("(2+(3*9))"))
print(check_parentheses("(2+(3*9)")) #스택에 소괄호가 하나 남아있어서 False
print(check_parentheses(")2+(3*9)("))