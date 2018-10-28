# Magic Index (CtCI/Chapter_8/8.3)

'''
	A magic index in an array A[0...n-1] is defined to be an index such thhat A[i] = i.
	Given a sorted array of distinct integers, write a method to find a magic index, if one exists
	Follow up: what if the values are not distinct?
'''

a = [-10, -8, 0, 3, 7, 7, 8, 10, 11, 12]
b = []
for i in range(len(a)):
    b.append(i)

def find_magic_index(a, b):
    mid = len(a)//2
    if a[mid] < b[mid]:
        return find_magic_index(a[mid:], b[mid:])
    elif a[mid] > b[mid]:
        return find_magic_index(a[:mid], b[:mid])
    else:
        return a[mid]

print(find_magic_index(a, b))

a = [-10, -8, 0, 1, 2, 3, 6, 8]
def MagicIndex(array, min, max):
    mid = (max + min) / 2
    print('mid: ')
    print(mid)
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return MagicIndex(array, mid + 1, max)
    if array[mid] > mid:
        return MagicIndex(array, min, mid - 1)


print MagicIndex(a, 0, len(a) - 1)
