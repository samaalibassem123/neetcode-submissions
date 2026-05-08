class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i, val in enumerate(tokens):
            if val not in operators:
                stack.append(val)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                eq = f'{str(val)}'.join([val2, val1])
                res = int(eval(eq))
                stack.append(str(res))
       
        print(stack[0])
        return int(stack[0])
