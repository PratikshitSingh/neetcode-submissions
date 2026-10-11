"""
Idea:
1. Count no. of 0:
    0s > 1: all zero,
    else: keep non zero product

2. Divide the product by the number.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        product = 1

        for num in nums:
            if num==0:
                zero_cnt += 1
            
            if zero_cnt > 1:
                product = 0
                break
            
            if num != 0:
                product *= num
        
        res = [0]*len(nums)
        if zero_cnt > 1: return res

        for i, num in enumerate(nums):
            if num != 0 and not zero_cnt:
                res[i] = product//num
            elif num != 0 and zero_cnt:
                res[i] = 0
            else:
                res[i] = product
        return res
            
