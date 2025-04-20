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
    
