class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        s=0;ma=min(nums)
        for i in nums:
            s+=i-ma
        return s
                    