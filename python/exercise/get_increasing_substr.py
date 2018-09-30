#给定一个长度为N的数组，找出一个最长的单调自增子序列。
#参考地址：http://www.felix021.com/blog/read.php?entryid=1587&page=1&part=1

#要求必须连续
def get_max_increasing_continuous_substr(arr):
    start = 0
    pos = 0
    length = 1
    res = []
    while pos < len(arr):
      if pos+1 < len(arr) and arr[pos] <= arr[pos+1]:
        length += 1
      else:
        res.append((start, length))
        start += length
        length =1
      pos += 1
    tmp = sorted(res, key=lambda x: x[1], reverse=True)[0]
    start = tmp[0]
    length = tmp[1]
    return arr[start:start+length]

print get_max_increasing_continuous_substr([9,8,3,4,5,6,7,10])

#不要求连续
def BinSearch(arr, value):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (left + right) / 2;
        if arr[mid] <= value:
            left = mid + 1
        else:
            right = mid - 1
    return left

def get_max_increasing_iscontinuous_substr(arr):
    res = [arr[0], ]
    item = 1

    while item < len(arr):
        if arr[item] > res[-1]:
            res.append(arr[item])
            item += 1
        else:
            left = BinSearch(res, arr[item])
            pos = item
            while arr[pos+1] < res[left]:
                pos += 1
            res[left:] = []
            res.extend(arr[item:pos+1])
            item = pos + 1
    return res


print get_max_increasing_iscontinuous_substr([2, 1, 6, 7, 3, 4, 5,  8,  9, 10])
