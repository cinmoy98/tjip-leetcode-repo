class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c_idx = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[c_idx] = nums[i]
                c_idx = c_idx+1
        while(c_idx<len(nums)):
            nums[c_idx]=0
            c_idx = c_idx+1