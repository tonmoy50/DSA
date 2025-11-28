class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens:
            if token == '+':
                second_param = stack.pop()
                first_param = stack.pop()
                stack.append(first_param + second_param)
            elif token == '-':
                second_param = stack.pop()
                first_param = stack.pop()
                stack.append(first_param - second_param)
            elif token == '*':
                second_param = stack.pop()
                first_param = stack.pop()
                stack.append(first_param * second_param)
            elif token == '/':
                second_param = stack.pop()
                first_param = stack.pop()
                stack.append(int(first_param / second_param))
            else:
                stack.append(int(token))
        
        return stack.pop()