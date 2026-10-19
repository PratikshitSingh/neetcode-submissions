class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, n = 0, 0, len(s)
        longest = 0
        ss = set()

        while r < n:
            if s[r] not in ss:
                ss.add(s[r])
                longest = max(longest, r-l+1) # {z,x} 0 1 2
                r += 1
            else:
                while s[r] in ss:
                    ss.remove(s[l])
                    l += 1
        return longest