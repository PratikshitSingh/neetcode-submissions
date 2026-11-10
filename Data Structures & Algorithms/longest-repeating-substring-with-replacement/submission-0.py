from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        l, r, results = 0, 0, 0

        while r < len(s):
            hashmap[s[r]] += 1

            if (r-l+1)-max(hashmap.values()) <= k:
                results = max(results, r-l+1)
                r += 1
            else:
                hashmap[s[l]] -= 1
                l += 1
                r += 1
        return results