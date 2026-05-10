class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i):
            ans=-inf
            if i==0:
                return 0
            for j in range(i):
                if abs(nums[j]-nums[i])<=target:
                    ans=max(ans,1+dfs(j))
            return ans

        n=len(nums)
        ans=dfs(n-1)
        return ans if ans>0 else -1