class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle=="" or haystack==needle):
            return 0
        
        needle_length = len(needle)
        haystack_length = len(haystack)
        first_char = needle[0]
        last_char = needle[needle_length-1]
        cur_index = 0
        
        if(needle_length == 1):
            return haystack.find(first_char)
        
        while(True):
            first_index = haystack.find(first_char, cur_index)
            last_index = first_index+needle_length-1
            
            if(first_index == -1 or last_index >= haystack_length):
                return -1
            
            if((last_index - first_index)+1 == needle_length):
                found = True
                for i in range(first_index, last_index+1):
                    if(haystack[i] != needle[i-first_index]):
                        found = False
                if(found):
                    return first_index
            cur_index+=1