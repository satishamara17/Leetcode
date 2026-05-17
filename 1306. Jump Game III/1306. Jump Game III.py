#
# Problem: 1306. Jump Game III
# Difficulty: Medium
# Link: https://leetcode.com/problems/jump-game-iii/submissions/2005703847/?envType=daily-question&envId=2026-05-17
# Language: python3
# Date: 2026-05-17


class Solution:  # class is used because the platform expects the method inside Solution
    def canReach(self, arr: List[int], start: int) -> bool:  # def is used to define the required function
        n = len(arr)  # number of indices in the array
        seen = [False] * n  # seen[i] tells whether index i is already visited
        q = deque([start])  # queue stores indices that I still need to process

        seen[start] = True  # start is marked visited before adding more moves

        while q:  # while is used to keep processing until no reachable index is left
            i = q.popleft()  # current index removed from the front of the queue

            if arr[i] == 0:
                return True  # True means I found an index with value 0

            for nxt in (i + arr[i], i - arr[i]):  # nxt takes both possible jump positions
                if 0 <= nxt < n and not seen[nxt]:
                    seen[nxt] = True  # mark this next index so I do not process it again
                    q.append(nxt)  # add this valid next index for later processing

        return False  # False means no reachable index has value 0
