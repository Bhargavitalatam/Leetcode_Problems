class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st=[]
        se=set()
        ls={c:i for i,c in enumerate(s)}
        for i,c in enumerate(s):
            if c not in se:
                while st and c<st[-1] and i<ls[st[-1]]:
                    se.discard(st.pop())
                se.add(c)
                st.append(c)
        return ''.join(st)
        