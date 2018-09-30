#-*- coding: utf-8 -*-

def mergesort(nums):
    # 归并排序
    length = len(nums)
    while length <= 1:
        return nums 
    mid = length / 2
    list1 = merge_sort(nums[: mid])
    list2 = merge_sort(nums[mid:])
    return merge(list1, list2)


def merge(list1, list2):
    res = []
    i = j = 0
    length1 = len(list1) 
    length2 = len(list2)
    while i < length1 and j < length2:
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    if i < length1:
        res += list1[i:]
    elif j < length2:
        res += list2[j:]
    return res

print merge_sort([])
print merge_sort([1])
print merge_sort([5,4])
print merge_sort([4,5])
print merge_sort([4,5,3])
print merge_sort([6,3,8,2,0])
