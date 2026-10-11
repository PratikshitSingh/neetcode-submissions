"""
Idea:
1. Use l, r pointers
2. Store the char in a set, until char already present in set.
3. move l+=1 and pop from set until its not present
4. whenever moving r, update the max_len

zxyzxyz
 l r

3

T: O(N)
s: O(M) unique characters in string

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        max_len = 1

        l, r = 0, 1
        seen = set()
        seen.add(s[l])

        while r < len(s):
            # print(seen)
            if s[r] in seen:
                while l<r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            else:
                seen.add(s[r])
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len