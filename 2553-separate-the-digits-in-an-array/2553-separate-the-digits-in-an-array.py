class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        r=[]
        for i in nums:
            d=list(map(int,str(i)))
            r+=d
        return r
        