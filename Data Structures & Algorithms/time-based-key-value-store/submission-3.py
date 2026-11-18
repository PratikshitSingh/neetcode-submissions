"""
Method-
1. l, r, m
2. a[m]==target
3. if a[m] < target: l=m
4. else target < a[m]: r=m-1

T: set-O(1); get-O(logn)
S: O(m*n)

dry run:
{
a: (1, h), 
}
"""
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value_list = self.hashmap.get(key)
        if not value_list: return ""
        l, r = 0, len(value_list)-1 # 0,0
        answer = ""

        while l<=r:
            m = (l+r)//2 # 0
            if timestamp==value_list[m][0]: 
                return value_list[m][1]
            elif value_list[m][0] < timestamp:
                answer = value_list[m][1]
                l=m+1
            else: r=m-1
        return answer
