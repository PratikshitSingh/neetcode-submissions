"""
Approach-
1. a1 -> idx++
2. a2 -> idx--
3. if sum == 0: return True

edge case-


T- O(n+m)
S- O(1) - constact 26 length array

Dry run-
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for si in s:
            arr[ord(si)-97] += 1
        print(arr)

        for ti in t:
            arr[ord(ti)-97] -= 1
        print(arr)
        
        return all(x == 0 for x in arr)