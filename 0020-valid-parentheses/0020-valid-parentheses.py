class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        for c in s:
            if c == '(' or c == '{' or c =='[':
                stack.append(c)
            if len(stack):
                if c == ')':
                    if stack.pop(-1) != '(':
                        return False
                elif c == '}':
                    if stack.pop(-1) != '{':
                        return False
                elif c == ']':
                    if stack.pop(-1) != '[':
                        return False
            else:
                return False
        
        return True if len(stack) == 0 else False