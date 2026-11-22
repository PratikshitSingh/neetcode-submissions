"""
Idea:
1. Use stack to append numbers.
2. Pop when a sign shows up, and append back the calculation result.

T: O(N)
S: O(N)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ("+", "-", "*", "/"):
                right = stack.pop()
                left = stack.pop()
                stack.append(str(eval(left+t+right)))
            else:
                stack.append(t)
        
        return int(stack.pop())