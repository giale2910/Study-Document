# Bai 1) 1528. Shuffle String
class Solution(object):
    def restoreString(self, s, indices):
        ls= ''
        for i in range(len(indices)):
            index = indices.index(i)
            ls += s[index]
        return ls
# class Solution:
#     def restoreString(self, s, indices) :
#         result = [None] * len(s)
#         for char, idx in zip(s, indices):
#             result[idx] = char
# 		return ''.join(result)

class Solution(object):
    def restoreString(self, s, indices):
        rs = ['']* len(s)
        for i , v in enumerate(s):
            rs[indices[i]] = v
        return ''.join(rs)
# Bai 3) 976. Largest Perimeter Triangle
class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
        
        
# Bai 4) 1491. Average Salary Excluding the Minimum and Maximum Salary    
class Solution(object):
    def average(self, salary):
        maxS = max(salary)
        minS = min(salary)
        sumS = 0.0 
        for i in salary:
            sumS += i
        return (sumS-maxS-minS) / (len(salary)-2)

class Solution(object):
    def average(self, salary):
        return (float(sum(salary)) - max(salary)-min(salary)) / (len(salary)-2)

class Solution(object):
    def average(self, salary):
        salary = sorted(salary)
        return float(sum(salary[1:-1])) / (len(salary) -2)

