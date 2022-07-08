class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1=0
        nums2=[]
        for i in nums:
            sum1+=i
            nums2.append(sum1)
        return nums2
            