class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=[[] for i in range(len(nums))];output=[];stack=[]
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        for i in set(nums):
            arr[count[i]-1].append(i)
        for i in arr:
            for j in i:
                stack.append(j)
        for l in range(k):
            if stack: output.append(stack.pop())
        return output