def positive(nums):
    positives = []
    for i in nums:
        if i > 0:
            positives.append(i)
    return positives

print(positive([-2, 5, -10, 12, -99]))