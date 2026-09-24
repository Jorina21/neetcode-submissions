class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} #create a dict 

        #membership check is O(1) because of keys

        #add number, index to dict
        #[4,3,5,8] target= 11    [1,3]

        for index, value in enumerate(nums): #enumerate gives index, value

            complement = target - value

            if complement in seen:
                return [seen[complement], index ]  #[1,3]

            seen[value] = index # {4:0,3:1,5:2,}
   


