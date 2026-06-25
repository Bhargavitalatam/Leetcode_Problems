class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return 0
        n=len(nums);co=0
        for i in range(n):
            frq=0
            for j in range(i,n):
                if nums[j]==target:
                    frq+=1
                if frq>(j-i+1)//2:
                    co+=1
        return co            
                

        