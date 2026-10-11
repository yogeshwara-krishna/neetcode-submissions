class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for s in strs:
            l=str(len(s))
            while len(l)<3: 
                l="0"+l
                # print("l : ",l)
            ans+=l
            ans+=s
        # print(ans)
        return ans
    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            if s[i:i+3].isdigit():
                end=int(s[i:i+3])
                ans.append(s[i+3:i+3+end])
                i=i+3+end
                # print(ans)
                # print(i)
        return ans

