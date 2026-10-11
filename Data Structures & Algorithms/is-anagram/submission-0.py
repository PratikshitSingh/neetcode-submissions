"""
Idea:
1. alphabets and their counts should be same.

T: O(n) lookup is O(1) for n elements.
S: O(n) store the alphabets in hashmap
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1
        
        for char in t:
            hashmap[char] -= 1
        
        for v in hashmap.values():
            if v != 0: return False
        return True