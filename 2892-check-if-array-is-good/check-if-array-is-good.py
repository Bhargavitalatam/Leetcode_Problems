class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        ch=list(range(1,n))
        nums=sorted(nums)
        return nums[-1]==n-1 and ch==nums[:-1]
        