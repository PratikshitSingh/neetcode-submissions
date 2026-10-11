"""
Idea:
1. For every value 1->max(piles): find the number of hours needed
2. naive: Iterate 1-> T: O(N*M) N: size of piles, M: max of pile
3. Instead of going linear on iterating h, let go binary search.
    -> m = l + (r-l)//2
    -> piles[i]/m > h, increase l
    -> else, decrease r
    -> stopping condition?

"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = l + (r-l)//2

            print(l, m , r)

            hours = 0
            for p in piles:
                hours += math.ceil(p/m)

            if hours > h:
                l = m+1
            else:
                res = m
                r = m-1
        
        return res
