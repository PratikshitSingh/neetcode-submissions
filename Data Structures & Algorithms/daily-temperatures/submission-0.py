"""
Idea:

Naive: O(N*N) - Use 2 nested loops

Optimized:
1. Think using stack
2. For a new temperature:
    -> Keep popping the stack while stack top < new temp
    -> subtract the current_index-index for finding no. of day
    -> insert (temp, current_index) in stack
3. everything left in stack will never see a higher temp


T: O(N)
S: O(N)

Edge case:
1. all decreasing

Dry run:

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, _ = stack.pop()
                days[idx] = i-idx
            stack.append((i, t))
        return days