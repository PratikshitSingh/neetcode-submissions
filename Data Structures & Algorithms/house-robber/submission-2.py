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
        
        money_n2 = 0
        money_n1 = 0

        for i in range(len(nums)):
            money = max(nums[i]+money_n2, money_n1) # 3
            money_n2 = money_n1 # 1
            money_n1 = money # 4
        return money_n1