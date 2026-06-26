class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums);ans=0;fre=[0]*(2*n+1)
        fre[n]=1
        p=n
        l=0
        for i in nums:
            if i==target:
                l+=fre[p]
                p+=1
            else:
                p-=1
                l-=fre[p]
            fre[p]+=1
            ans+=l
        return ans
                    