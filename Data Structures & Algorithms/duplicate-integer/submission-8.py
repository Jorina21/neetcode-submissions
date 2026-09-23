class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        my_set = set(num for num in nums)  # {expression for item in iterable}

        if len(my_set) != len(nums):
            return True

        
        return False



