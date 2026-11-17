class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            length=len(word)
            result=result+str(length)+'#'+word
        return result

    def decode(self, s: str) -> List[str]:
        i=0;new_result=[]
        while i<len(s):
            j=i;length=0
            while (s[j]!='#'):
                length=length*10+int(s[j])
                j+=1
            j+=1
            newstr="";cur=0
            while cur<length:
                newstr=newstr+s[j]
                cur+=1
                j+=1
            i=j
            new_result.append(newstr)
        return new_result
