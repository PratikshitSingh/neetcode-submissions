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
                s.add(ch)
            else:
                if not s:
                    return False
                if pair[ch] != s.top():
                    return False
                s.pop()
        return not s