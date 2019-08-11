class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack = list(haystack)
        # found = []
        # for n in needle:
        #     if n != haystack[-1]:
        #         haystack.pop()
        #     found.append(haystack[-1])
        #     # found.append(n)
        #     # found.append(haystack.index(n))
        # print(found)
        # # if len(found) == len(needle):
        # #     return haystack.index()
        # # else:
        # #     return -1
        # return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1