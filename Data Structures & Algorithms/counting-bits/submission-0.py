class Solution:
    def countBits(self, n: int) -> List[int]:
        # [0,1, 1,2, 1,2,2,3, 1,2,2,3,2,3,3,4, 1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5]

        def check_bits(x):
            cnt = 0
            while x:
                cnt += x&1
                x=x>>1
            return cnt

        cnts = []
        for i in range(n+1):
            cnts.append(check_bits(i))
        return cnts
