class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0;i=0;n=len(costs)
        while coins>0 and i<n:
            if coins-costs[i]<0:
                break
            else:
                c+=1
                coins-=costs[i]
            i+=1
        return c
        