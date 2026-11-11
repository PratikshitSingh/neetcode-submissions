class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        pair = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                if pair[ch] != stack[-1]:
                    return False
                stack.pop()
        return not stack