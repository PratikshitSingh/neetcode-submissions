class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        1. repitition is allowed.
        2. store sum and items with backtracking.

        T: O(n!)
        S: O(n!)
        """

        results = set()
        items = []
        total = 0

        def dfs(total, idx, items):
            if total > target: 
                return
            
            if total == target:
                items.sort()
                results.add(tuple(items))
                return

            for i in range(idx, len(nums)):
                num = nums[i]
                total += num
                items.append(num)
                
                dfs(total, i, items)
                
                total -= num
                items.remove(num)
        
        dfs(total, 0, items)
        return [list(tup) for tup in list(results)]
