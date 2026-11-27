class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Method- 
        1. at every point 2 choice - rob or leave
            => store these 2 choices via a max
            => f(N) = max( nums[N]+f(N-2), f(N-1) )

        T: O(N)
        S: O(1)
        """
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums)
        
        money_n2 = nums[0] # 2
        money_n1 = max(nums[0], nums[1]) # 1

        for i in range(2, len(nums)):
            money = max(nums[i]+money_n2, money_n1) # 3
            money_n2 = money_n1 # 1
            money_n1 = money # 4
        return money