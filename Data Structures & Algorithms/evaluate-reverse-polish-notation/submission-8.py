"""
Use stack to store the elements

T: O(N)
S: O(N)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for t in tokens:
            if t in ("+-*/"):
                t1 = stack.pop()
                t2 = stack.pop()
                
                match t:
                    case "+":
                        stack.append(t2+t1)
                    case "-":
                        stack.append(t2-t1)
                    case "*":
                        stack.append(t2*t1)
                    case "/":
                        stack.append(int(t2/t1))
            else:
                stack.append(int(t))
        return stack.pop()
