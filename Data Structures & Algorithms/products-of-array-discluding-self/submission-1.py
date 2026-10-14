"""
Approach - 
Prefix and Suffix products

T - O(N)
S - O(N)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]

        for i in range(n):
            prefix[i] = (prefix[i-1] if i else 1) * nums[i]

        for i in range(n-1, -1, -1):
            suffix[i] = (suffix[i+1] if i+1<n else 1) * nums[i]

        results = [1 for _ in range(n)]
        for i in range(n):
            results[i] = (prefix[i-1] if i else 1) * (suffix[i+1] if i+1<n else 1)
        return results