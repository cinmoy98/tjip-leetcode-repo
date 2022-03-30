# Problem Link : https://leetcode.com/problems/kth-largest-element-in-an-array/
# Problem Number : 215
# Problem Tag : Array, Heap
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 30/3/2022

# Approach 1 (Using heap)
################################################################
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        k=k-1
        while(k>0):
            heapq.heappop(nums)
            k=k-1
        return -nums[0]