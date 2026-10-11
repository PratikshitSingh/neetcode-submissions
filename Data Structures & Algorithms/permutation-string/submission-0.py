"""
idea:
1. map s1 to m1, len l
2. map substring of len l in s2 to m2 & if map m2 matchs m1: true

T: O(N) -> length of longer string s2
S: O(M) -> length of shorted string s1
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = [0]*26
        l1 = len(s1)
        for s in s1: 
            m1[ ord(s)-ord('a') ] += 1

        m2 = [0]*26
        for s in s2[:l1-1]: 
            m2[ ord(s)-ord('a') ] += 1
        
        l, r = 0, l1-1
        while r < len(s2):
            s = s2[r]
            m2[ ord(s)-ord('a') ] += 1

            if m1 == m2: return True

            s = s2[l]
            m2[ ord(s)-ord('a') ] -= 1
            l += 1
            r += 1
        return False

