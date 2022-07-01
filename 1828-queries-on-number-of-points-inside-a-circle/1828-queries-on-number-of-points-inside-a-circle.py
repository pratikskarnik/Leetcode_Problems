class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        counts=[]
        for q in queries:
            iq,jq,r=q
            c=0
            for point in points:
                i,j=point
                if (iq-i)**2+(jq-j)**2<=r**2:
                    c+=1
            counts.append(c)
        return counts
                    
                    
        