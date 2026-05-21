class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1=set()
        ma=0
        for i in arr1:
            while i>0:
                set1.add(i)
                i//=10
        for i in arr2:
            while i>0:
                if i in set1:
                    ma=max(ma,len(str(i)))
                    break
                i//=10
        return ma

        