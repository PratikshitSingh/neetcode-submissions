"""
Idea:
1. time = d/s
2. sort in decreasing order of position
3. 

"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine = [(p, s) for p, s in zip(position, speed)]
        combine.sort(key = lambda x: -x[0])

        time = [(target-p)/s for p, s in combine]
        print(time)

        cnt = 1
        blocker = time[0]

        for t in time[1:]:
            if blocker >= t:
                continue
            else:
                cnt += 1
                blocker = t
        
        return cnt
