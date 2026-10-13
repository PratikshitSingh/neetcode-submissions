"""
Approach-
1. map: key = (freq_i,)*26, value = [words...]

T- O(m * n)
S - O(m)

Dry run-

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for string in strs:
            tup = [0]*26
            for ch in string:
                tup[ord(ch)-97] += 1

            mapper[tuple(tup)].append(string)
        return list(mapper.values())