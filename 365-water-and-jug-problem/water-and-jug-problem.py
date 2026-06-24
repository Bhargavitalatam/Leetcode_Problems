class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        import math
        z=math.gcd(x,y)
        if x+y<target:
            return False
        if target%z==0:
            return True
        return False
            
        