def hasBalancedParentheses(exp):
    cnt = 0
    for item in exp:
        if item == '(':
            cnt += 1
        elif item == ')':
            cnt -= 1
        if cnt < 0:
            return False #오른쪽괄호가 많게 되면 어떻게 하든 괄호 수가 안맞음. 0이어야함
    if cnt == 0:
        return True
    else:
        return False #맞나 이거...
print('(())()', hasBalancedParentheses('(())()'))
print('((()())())', hasBalancedParentheses('((()())())'))
print(')()()', hasBalancedParentheses(')()()'))
