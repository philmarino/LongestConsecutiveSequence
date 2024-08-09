def longestConsecutive(nums):
    nums.sort()

    streakLength = 0
    longestStreak = 0
    previous = nums[0] + 1 #to cause the

    for item in nums:
        if streakLength == 0:
            previous = item
            streakLength = 1
            continue
        if item == previous + 1:
            streakLength += 1
            previous = item
        else: #streak just ended and a new one starts
            if streakLength > longestStreak:
                longestStreak = streakLength
            streakLength = 1
            previous = item

    if streakLength > longestStreak:
        longestStreak = streakLength

    return longestStreak


# Example 1:
# Input: 
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: 
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
# Output: 9
 
