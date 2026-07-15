class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o,e=[],[]
        for i in range(1,2*n+1):
            if i%2:
                o.append(i)
            else:
                e.append(i)
        import math
        return math.gcd(sum(o),sum(e))
        