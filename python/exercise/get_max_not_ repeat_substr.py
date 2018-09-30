#从一个字符串中找到一个连续子串，该子串中任何两个字符不能相同，求子串的最大长度并输出一条最长不重复子串。

def test(arr):
    pos = 0
    length = 1
    res = []
    count = 0
    res.append(arr[pos])

    while pos < len(arr):
        if pos+1 < len(arr):
            if arr[pos+1] not in res[count]:
                length += 1
                res[count] += arr[pos+1]
            else:
                length = 1
                count += 1
                if count+1 != len(res):
                    res.append(arr[pos+1])
                else:
                    res[count] += arr[pos+1]
        pos += 1

    tmp = sorted(res, key=lambda x: len(x), reverse=True)[0]
    return tmp, len(tmp)

print test("abdffd")
print test("absd")
print test("abcaacdeabacdefg")
