class Solution:
    def check(self, nums: List[int]) -> bool:
        ch=sorted(nums)
        n=len(nums)
        for i in range(n):
            if nums[n-1-i:]+nums[:n-1-i]==ch:
                return True
        return False
        