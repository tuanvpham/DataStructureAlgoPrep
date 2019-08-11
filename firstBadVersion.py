def firstBadVersion(self, n):
    low = 1
    high = n
    mid = math.ceil((high + low)/2)
    while(mid > low and high > mid):
        if(isBadVersion(mid) == False):
            low = mid
            mid = math.ceil((high + low)/2)
        else:
            high = mid
            mid = math.ceil((high + low)/2)
    if(high-low == 0):
        return low
    if(high-low == 1):
        if(isBadVersion(low)):
            return low
        else:
            return high
    return mid