"""数组最大和次大值"""

def get_max_and_second(nums):
    length = len(nums)
    if not nums or length == 1:
        return

    first = nums[0]
    second = nums[1]
    if first < second:
        first, second = second, first
    if length == 3:
        return first, second

    for val in nums[3:]:
        if val > second:
            second = val
            if second > first:
                first, second = second, first
    return first, second

print get_max_and_second([])
print get_max_and_second([2, 1])
print get_max_and_second([5, 4, 3, 2])
print get_max_and_second([3, 7, 5, 1])


def get_max_and_second_1(nums):
    length = len(nums)
    if not nums:
        return

    first = nums[0]
    if length == 1:
        second = float("inf")
        return first, second
    elif length == 2:
        second = nums[1]
        if first < second:
            first, second = second, first
        return first, second

    mid = len(nums) / 2
    leftmax, leftsecond = get_max_and_second_1(nums[0:mid])
    rightmax, rightsecond = get_max_and_second_1(nums[mid:])
    if leftmax < rightmax:
        first = rightmax
        second = leftmax if leftmax > rightsecond else rightsecond
    elif rightmax < leftmax:
        first = leftmax
        second = rightmax if rightmax > leftsecond else leftsecond
    return first, second

print get_max_and_second_1([])
print get_max_and_second_1([1])
print get_max_and_second_1([2, 1])
print get_max_and_second_1([5, 4, 3, 2])
print get_max_and_second_1([3, 7, 5, 1, 2])
