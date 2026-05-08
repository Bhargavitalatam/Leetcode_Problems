class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        cu=far=ju=0
        for i in range(n-1):
            far=max(far,i+nums[i])
            if i==cu:
                ju+=1
                cu=far
        return ju
        