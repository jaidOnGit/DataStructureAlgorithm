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
    
class ContainsDuplicate:
    def __str__(self):
        return """
        217. Contains Duplicate
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
        """
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {key: 0 for key in nums}
        for i in range(len(nums)):
            if hash_table.get(nums[i], 0) == 1:
                return True
            hash_table[nums[i]] += 1
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        pythonic_approach = True
        if pythonic_approach:
            return len(set(nums)) != len(nums)
            
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

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

class FindPivotIndex:
    def __str__(self):
        return """
    724. Find Pivot Index
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.
    """

    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)):
            total_sum+= nums[i]

        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i    
            left_sum += nums[i]    
        return -1
    
class LargestNumberAtLeastTwiceOfOthers:
    def __str__(self):
        return """
        747. Largest Number At Least Twice of Others
        You are given an integer array nums where the largest integer is unique.

        Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
        """

    def dominantIndex(self, nums: List[int]) -> int:
        max_num = 0
        max_numIdx = 0
        for i in range(len(nums)):
            if max_num < nums[i]:
                max_num = nums[i]
                max_numIdx = i
        
        for i in range(len(nums)):
            if nums[i] != max_num and max_num < 2*nums[i]:
                return -1
        return max_numIdx
    
class PlusOne:
    def __str__(self):
        return """
        66. Plus One
        You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

        Increment the large integer by one and return the resulting array of digits.
        """
    
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        n = len(digits) - 1
        for i in range(len(digits)):
            if n >= 0:
                number += (digits[i]*(10**n))
                n -= 1
                
        num_list = list()
        new_num = number + 1
        while (new_num != 0):
            num_list.append(new_num%10)
            new_num = new_num // 10
        
        # reverse list
        n = len(num_list) - 1
        for i in range(len(num_list)//2):
            num_list[i], num_list[n-i] = num_list[n-i], num_list[i]
        return num_list
    
class DiagonalTraverse:
    def __str__(self):
        return """
        498. Diagonal Traverse
        Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
        """
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        def getDiagonal(mat, i, j, M, N, forward=True):
            diagonal_elements = list()
            while i < M and j >= 0:
                diagonal_elements.append(mat[i][j])
                i += 1
                j -= 1
            if forward:
                return diagonal_elements
            else:
                n = len(diagonal_elements) - 1
                for i in range(len(diagonal_elements)//2):
                    diagonal_elements[i], diagonal_elements[n-i] = diagonal_elements[n-i], diagonal_elements[i]
                return diagonal_elements

        M = len(mat)
        N = len(mat[0])

        diagonal_order = list()
        direction = 0
        i = 0
        for j in range(N):
            diagonal_order.extend(getDiagonal(mat,i,j,M,N,forward=(direction%2==1)))
            direction += 1
        j = N-1
        for i in range(1,M):
            diagonal_order.extend(getDiagonal(mat,i,j,M,N,forward=(direction%2==1)))
            direction += 1
        return diagonal_order


    