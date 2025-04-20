class Sorting:
    def __init__(self, array, sorting='bubble'):
        self.array = array
        if sorting == 'bubble':
            self.bubble_sort()

    def bubble_sort(self):
        """
        Bubble Sort compares adjacent elements in the list:
        Starting from the beginning, compare each pair of elements.
        If the current element is larger than the next, swap them.
        After completing one pass, the largest element "bubbles up" to its correct position at the end.
        Repeat the process for the remaining unsorted portion of the list until no swaps occur.
        """
        size = len(self.array)
        for s in range(size-1):
            swap = False
            for i in range(size-1-s):
                if self.array[i] > self.array[i+1]:
                    swap = True
                    temp = self.array[i+1]
                    self.array[i+1] = self.array[i]
                    self.array[i] = temp
            if not swap:
                break

    def insertion_sort(self):
        """
        sorting deck of cards

        It builds the final sorted list one item at a time by repeatedly picking an unsorted element and 
        inserting it into its correct position in the sorted portion of the list.
        Divide the list into two parts: a sorted portion (left) and an unsorted portion (right).
        Iterate through the unsorted portion, inserting elements into the correct position within the sorted portion.

        Start with the second element (index 1) as the key element.
        Compare the key element with elements in the sorted portion.
        Shift all larger elements to the right to make space for the key element.
        Insert the key element into its correct position.
        Repeat until all elements are sorted.
        """
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1 
            while j >= 0 and self.array[j] > key:
                self.array[j+1] = self.array[j] 
                j = j - 1
            self.array[j+1] = key
        
    
    def shell_sort(self):
        pass

    def selection_sort(self):
        """
        Divide the list into two parts: sorted and unsorted.
        Find the smallest (or largest) element in the unsorted portion.
        Swap it with the first unsorted element.
        Repeat until all elements are sorted.
        Start from the first element of the list.
        Find the smallest element in the remaining unsorted portion.
        Swap the smallest element with the first unsorted element.
        Move to the next unsorted element and repeat.
        """
        for i in range(len(self.array)):
            min_index = i
            for j in range(i+1, len(self.array)):
                if self.array[min_index] > self.array[j]:
                    min_index = j
            temp = self.array[i]
            self.array[i] = self.array[min_index]
            self.array[min_index] = temp

    def _merge_sort(self, arr):
        """
        
        """
        # Base case: A single element or empty array is already sorted
        if len(arr) <= 1:
            return arr

        # Step 1: Divide the array into two halves
        mid = len(arr) // 2
        left_half = self._merge_sort(arr[:mid])  # Recursively sort the left half
        right_half = self._merge_sort(arr[mid:])  # Recursively sort the right half

        # Step 2: Merge the two sorted halves
        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        # Create a new list to hold the merged elements
        sorted_array = []
        i = j = 0

        # Step 3: Compare elements from both halves and merge them in sorted order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        # Step 4: Add remaining elements from the left half
        while i < len(left):
            sorted_array.append(left[i])
            i += 1

        # Step 5: Add remaining elements from the right half
        while j < len(right):
            sorted_array.append(right[j])
            j += 1

        return sorted_array
    

    def quick_sort(self, arr):
        # Base case: If the array has 1 or no elements, it's already sorted
        if len(arr) <= 1:
            return arr

        # Choose the first element as the pivot
        pivot = arr[0]

        # Partition the array into left (<= pivot) and right (> pivot)
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]

        # Recursively sort the left and right partitions and combine them
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)
    
    def quick_select(self, arr, k):
        """
        Find the k-th smallest element in an array using Quick Select, choosing the first element as pivot.

        :param arr: List of elements.
        :param k: Position of the k-th smallest element (1-based index).
        :return: The k-th smallest element.
        """
        # Base case: If the array has one element, return it
        if len(arr) == 1:
            return arr[0]

        # Step 1: Choose the first element as the pivot
        pivot = arr[0]

        # Step 2: Partition the array
        left = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to pivot
        right = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot

        # Step 3: Determine the position of the pivot
        if len(left) + 1 == k:  # Pivot is the k-th smallest
            return pivot
        elif len(left) >= k:  # k-th smallest is in the left partition
            return self.quick_select(left, k)
        else:  # k-th smallest is in the right partition
            return self.quick_select(right, k - len(left) - 1)

    def heap_sort(self):
        pass
