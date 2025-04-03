def negative(nums):
    negatives = []
    for i in nums:
        if i < 0:
            negatives.append(i)
    return negatives

print(negative([-2, 5, -10, 12, -99]))