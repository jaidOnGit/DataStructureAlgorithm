from typing import List

class ProblemInArray:
    def getWaveArray(self, array):
        """
        Given an unsorted array of integers, 
        sort the array into a wave array. 
        An array arr[0..n-1] is sorted in wave form if: arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..
        """
        # if array is sorted and we swap even order a wave can be created
        # 1 2 3 4 5 6 7 8 --> 1 3 2 5 4 7 6 8
        
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1 
            while j >= 0 and array[j] > key:
                array[j+1] = array[j] 
                j = j - 1
            array[j+1] = key

        for i in range(1,len(array),2):
            temp = array[i-1]
            array[i-1] = array[i]
            array[i] = temp

        return array
    
    def matchSubArraySum(self, arr, sumvalue):
        """
        Given a 1-based indexing array arr[] of non-negative integers and an integer sum. 
        You mainly need to return the left and right indexes(1-based indexing) of that subarray. 
        In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. 
        If no such subarray exists return an array consisting of element -1.
        """
        def sumOfArray(array):
            temp = 0 
            for i in range(len(array)):
                temp += array[i]
            return temp
        
        for i in range(0,len(arr)-size):
            for size in range(1,len(arr)):
                subarray = arr[i:i+size]
                if sumOfArray(subarray) == sumvalue:
                    return [i, i+size]
        return [-1]
    
class TwoSum:
    def __str__(self):
        return """
        1. Two Sum
        Given an array of integers nums and an integer target, 
        return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        """
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        BruteForce
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        A simple implementation uses two iterations. 
        In the first iteration, we add each element's value as a key and its index as a value to the hash table. 
        Then, in the second iteration, we check if each element's complement (target−nums[i]) exists in the hash table. 
        If it does exist, we return current element's index and its complement's index. 
        Beware that the complement must not be nums[i] itself!
        Time complexity: O(n)
        Space complexity: O(n)
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []
    
class RemoveDuplicates:
    def __str__(self):
        return """
        26. Remove Duplicates from Sorted Array
        Given an integer array nums sorted in non-decreasing order, 
        remove the duplicates in-place such that each unique element appears only once. 
        The relative order of the elements should be kept the same. 
        Then return the number of unique elements in nums.
        
        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

        Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
        Return k.
        Custom Judge:

        The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
        If all assertions pass, then your solution will be accepted.
        """
    
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] < nums[i]:
                nums[j + 1] = nums[i]
                j += 1
        
        return j + 1
    
class RemoveElement:
    def __str__(self):
        return """
        27. Remove Element
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

        Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

        Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
        Return k.
        """
    
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = len(nums) 
        # i = 0
        # while i < k:
        #     if nums[i] == val:
        #         nums[i] = nums[k-1]
        #         k -= 1
        #     else: # if i & k both are equal then need to check again for i
        #         i += 1
        # return k
        # in-place : 2 pointer problem
        writer = 0 # writer pointer
        for reader in range(len(nums)): # read 
            if nums[reader] != val:
                nums[writer] = nums[reader] # write only when non match condition is True
                writer += 1
        return writer

class SearchInsertPosition:
    def __str__(self):
        return """
        35. Search Insert Position
        Given a sorted array of distinct integers and a target value, return the index if the target is found. 
        If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.
        """
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left