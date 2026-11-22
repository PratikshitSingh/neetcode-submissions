class Solution:
    def isValid(self, s: str) -> bool:
        s = collections.deque ()
        pair = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for ch in s:
            if ch in ('(', '[', '{'):
                s.append(ch)
            else:
                if not s:
                    return False
                if pair[ch] != s.peek():
                    return False
                s.pop()
        return not s