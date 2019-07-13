class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        look_up_table = {}
        for num in nums:
            if num in look_up_table:
                look_up_table[num] += 1
            else:
                look_up_table[num] = 1
        
        for k, v in look_up_table.items():
            if v != 1:
                for i in range(v-1):
                    nums.remove(k)
        return len(nums)