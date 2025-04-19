class Heap:
    """
    Abstract Data Type: Heap

    A heap is a special tree-based data structure that satisfies the heap property:
      - In a Max-Heap, the parent node is greater than or equal to its children.
    
    Applications:
      - Priority queues, sorting algorithms (Heap Sort), and graph algorithms.
    
    Limitations:
      - Operations like insertion and deletion take O(log n).
      - Random access is inefficient compared to arrays.

    This class provides methods to create and operate on a Max-Heap.
    """

    def __init__(self):
        """
        Initialize an empty heap.
        """
        self.heap = []

    def insert(self, value):
        """
        Insert an element into the heap and maintain the heap property.

        :param value: The value to insert.
        :return: None
        """
        self.heap.append(value)  # Add the value at the end
        self._heapify_up(len(self.heap) - 1)  # Restore the heap property

    def extract_max(self):
        """
        Remove and return the maximum element from the heap.

        :return: The maximum value.
        :raises IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Extract from an empty heap")

        max_value = self.heap[0]  # The root (maximum element)
        self.heap[0] = self.heap[-1]  # Move the last element to the root
        self.heap.pop()  # Remove the last element
        self._heapify_down(0)  # Restore the heap property
        return max_value

    def peek_max(self):
        """
        Retrieve the maximum element without removing it.

        :return: The maximum value.
        :raises IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Peek from an empty heap")
        return self.heap[0]

    def size(self):
        """
        Return the number of elements in the heap.

        :return: The size of the heap.
        """
        return len(self.heap)

    def is_empty(self):
        """
        Check if the heap is empty.

        :return: True if the heap is empty, False otherwise.
        """
        return len(self.heap) == 0

    def _heapify_up(self, index):
        """
        Restore the heap property moving upwards.

        :param index: The index of the element to heapify.
        :return: None
        """
        parent_index = (index - 1) // 2  # Find the parent index
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            # Swap the current element with its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Recursively heapify up
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """
        Restore the heap property moving downwards.

        :param index: The index of the element to heapify.
        :return: None
        """
        largest = index
        left_child = 2 * index + 1  # Left child index
        right_child = 2 * index + 2  # Right child index

        # Compare with the left child
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        # Compare with the right child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        # If the largest element is not the current index
        if largest != index:
            # Swap with the largest child
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # Recursively heapify down
            self._heapify_down(largest)

def test_heap():
    # Instantiate the Heap class
    heap = Heap()

    # Example 1: Insert elements into the heap
    heap.insert(10)
    heap.insert(30)
    heap.insert(20)
    heap.insert(5)
    print("\nHeap after insertion (Max-Heap):", heap.heap)

    # Example 2: Peek at the maximum element
    max_element = heap.peek_max()
    print("\nMaximum element (peek):", max_element)

    # Example 3: Extract the maximum element
    extracted_max = heap.extract_max()
    print("\nExtracted maximum element:", extracted_max)
    print("Heap after extracting maximum:", heap.heap)

    # Example 4: Check the size of the heap
    heap_size = heap.size()
    print("\nSize of the heap:", heap_size)

    # Example 5: Check if the heap is empty
    is_empty = heap.is_empty()
    print("\nIs the heap empty?", is_empty)
