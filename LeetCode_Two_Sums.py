def largestSum(nums, t):
    myDict = {}

    for i, num in enumerate(nums):
        if t - num in myDict:
            return (num, t-num)
        else:
            myDict[num] = i
    return -1,-1

print(largestSum([1, 3, 4, 6, 3], 6))