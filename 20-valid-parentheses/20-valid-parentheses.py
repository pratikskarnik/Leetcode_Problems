class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"}":"{",")":"(","]":"["}
        for i in s:
            stack.append(i)
            if i in [")","]","}"]:
                if len(stack)>1:
                    ele=stack.pop()
                    ele2=stack.pop()
                    if d[ele]!=ele2:
                        return False
                else:
                    return False
        
        return len(stack)==0
        
        