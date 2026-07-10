class Solution:
    def numRabbits(self, a: List[int]) -> int:
        from collections import Counter
        from math import ceil
        t=0
        c=Counter(a)
        for i,j in c.items():
            gs=i+1
            g=ceil(j/gs)
            t+=gs*g
        return t