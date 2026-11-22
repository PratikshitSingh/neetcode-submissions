"""
Use stack to store the elements

T: O(N)
S: O(N)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for t in tokens:
            if t.isnumeric():
                stack.append(t)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                t3 = eval(t2 + t + t1)
                stack.append(str(t3))
        return int(stack.pop())
