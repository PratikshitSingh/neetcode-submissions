"""
T: O(26*N)
S: O(1)
"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_fix = Counter(s1)
        l, r = 0, len(s1)-1
        hashmap_move = Counter(s2[l:r])

        while r < len(s2):
            hashmap_move[s2[r]] += 1
            # print(hashmap_fix, hashmap_move)
            if (hashmap_fix == hashmap_move):
                return True
            else:
                hashmap_move[s2[l]] -= 1
                l += 1
                r += 1

        return False