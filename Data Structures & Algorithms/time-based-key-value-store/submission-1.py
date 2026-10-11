"""
Idea:
1. Use a dict of list to store the inputs.
2. for get:
    -> since timestamp are sorted, use O(logn) binary search
    -> l, r
    -> m
    -> res = a[l]

    -> a[m] == ts
    -> a[l] <= ts < a[m]: (equality for smaller array)
        - res = max(res, a[l])
        - r = m-1
    -> else:
        - res = max(res, a[m])
        - l = m+1
    return res


T:
set: O(1)
get: O(logn
"""
class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))
        return

    def get(self, key: str, timestamp: int) -> str:
        
        def bs(nums, ts):
            l, r = 0, len(nums)-1
            if not nums or ts < nums[l][0]: 
                return ""
            
            res = ""
            
            while l <= r:
                m = l + (r-l)//2

                if timestamp == nums[m][0]:
                    return nums[m][1]
                
                elif nums[m][0] < timestamp:
                    # res = max(res, nums[l][1])
                    res = nums[m][1]
                    l = m + 1
                else:
                    r = m - 1
            return res


        return bs(self.hash_map[key], timestamp)
