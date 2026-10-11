"""
Idea:
only lowercase English letters

1. Group by anagrams.
2. Create hashmap:
    -> key: frequency map
    -> value: list of string

T: O(n*m)
S: O(n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_map = defaultdict(list)

        for s in strs:
            mini_map = [0]*26
            for c in s:
                mini_map[ord(c) - ord('a')] += 1
            
            master_map[tuple(mini_map)].append(s)
        return list(master_map.values())
