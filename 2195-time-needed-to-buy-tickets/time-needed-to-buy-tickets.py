from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        c=0
        q=deque()
        for i in range(len(tickets)):
            q.append(i)
        while q:
            e=q.popleft()
            tickets[e]-=1
            c+=1
            if tickets[e]>0:
                q.append(e)
            if tickets[e]==0 and e==k:
                return c                

        