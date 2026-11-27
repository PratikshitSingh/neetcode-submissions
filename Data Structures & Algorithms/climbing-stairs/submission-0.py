class Solution:
    def climbStairs(self, n: int) -> int:
        """
        DP - f(N) = f(N-2) + f(N-1)
        """
        if n==1 or n==2: return n

        res_n2 = 1
        res_n1 = 2
        res = 0
        for i in range(3, n+1):
            res = res_n1 + res_n2
            res_n2 = res_n1
            res_n1 = res
        return res
