class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[];ma=0
        for i in range(len(heights)+1):
            ch=0 if i==len(heights) else heights[i]
            while st and heights[st[-1]]>ch:
                h=heights[st.pop()]
                w=i if not st else i-st[-1]-1
                ma=max(ma,h*w)
            st.append(i)
        return ma
        