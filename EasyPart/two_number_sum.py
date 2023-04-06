
#  O(n^2) time | O(1) space
# def twoNumberSum(array, targetSum): 
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum: 
#                 return [firstNum, secondNum]

#     return []


# 
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []
