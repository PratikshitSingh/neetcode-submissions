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
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(int(a / b))  # truncates toward zero
            else:
                stack.append(int(t))

        return stack.pop()