# https: // leetcode.com/problems/remove-duplicates-from-sorted-array/
# Sample: [0,0,1,1,1,2,2,3,3,4]

# This solution requires us to return length of sorted array without duplication and modify the given array without allocating new array, but allow to have O(1) extra memory
# Hence, I used dictionary to look up the numbers, remove duplication in given array, and return the length of modified array
# However, other people's solutions do not remove duplication, but use an variable to count
# Do we really need to remove the duplication as the problem told?

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

# nums arr: [0,1,2,3,4]
# result: array length


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        idx = 1
        last_num = nums[0]
        for i in range(1, len(nums)):
            if last_num != nums[i]:
                last_num = nums[i]
                nums[idx] = last_num
                idx += 1
            print(nums)
        return idx

# nums arr: [0,1,2,3,4,2,2,3,3,4]
# idx: 5
# result: count idx
