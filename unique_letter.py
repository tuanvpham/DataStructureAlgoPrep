# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        look_up_table = {}
        for c in s:
            if c in look_up_table:
                look_up_table[c] += 1
            else:
                look_up_table[c] = 1
        for k, v in look_up_table.items():
            if v == 1:
                return s.index(k)
        return -1
