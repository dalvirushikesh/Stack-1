#Time Complexity = O(n)
#Space Complexity = O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n  # Initialize result array with -1
        stack = []  # Stack to keep indices
        
        for i in range(2 * n):  # Loop twice for circular array
            while stack and nums[i % n] > nums[stack[-1]]:  # Find the next greater element
                popped = stack.pop()
                res[popped] = nums[i % n]
            if i < n:
                stack.append(i)  # Push only indices in the first pass
        
        return res