class PriorityQueue:
    """
    Abstract Data Type: Priority Queue

    A priority queue is a data structure where each element is associated with a priority.
    Elements are dequeued based on their priority. This implementation uses a Max-Heap 
    for efficient priority-based processing.

    Applications:
      - Task scheduling, graph algorithms (Dijkstra, Prim), and data compression (Huffman coding).
    
    Limitations:
      - Direct random access to elements is inefficient.
      - Adjusting priorities may require reordering.
    """

    def __init__(self):
        """
        Initialize an empty priority queue.
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Insert an element into the priority queue with a given priority.

        :param value: The value to insert.
        :param priority: The priority of the value.
        :return: None
        """
        self.queue.append((priority, value))
        self._heapify_up(len(self.queue) - 1)

    def dequeue(self):
        """
        Remove and return the element with the highest priority.

        :return: The value with the highest priority.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty priority queue")

        highest_priority_value = self.queue[0][1]
        # Move the last element to the root and pop the last element
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self._heapify_down(0)
        return highest_priority_value

    def peek(self):
        """
        Retrieve the element with the highest priority without removing it.

        :return: The value with the highest priority.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty priority queue")
        return self.queue[0][1]

    def is_empty(self):
        """
        Check if the priority queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the number of elements in the priority queue.

        :return: The size of the queue.
        """
        return len(self.queue)

    def _heapify_up(self, index):
        """
        Restore the heap property moving upwards.

        :param index: The index of the element to heapify.
        :return: None
        """
        parent = (index - 1) // 2
        if index > 0 and self.queue[index][0] > self.queue[parent][0]:
            self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """
        Restore the heap property moving downwards.

        :param index: The index of the element to heapify.
        :return: None
        """
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.queue) and self.queue[left][0] > self.queue[largest][0]:
            largest = left
        if right < len(self.queue) and self.queue[right][0] > self.queue[largest][0]:
            largest = right

        if largest != index:
            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self._heapify_down(largest)

def test_priorityqueue():
    # Instantiate the PriorityQueue class
    priority_queue = PriorityQueue()

    # Example 1: Enqueue elements into the queue
    priority_queue.enqueue("Task1", 3)
    priority_queue.enqueue("Task2", 5)
    priority_queue.enqueue("Task3", 1)
    priority_queue.enqueue("Task4", 4)
    print("\nPriority Queue after enqueue operations:", priority_queue.queue)

    # Example 2: Peek at the element with the highest priority
    highest_priority_task = priority_queue.peek()
    print("\nElement with the highest priority (peek):", highest_priority_task)

    # Example 3: Dequeue the element with the highest priority
    dequeued_task = priority_queue.dequeue()
    print("\nDequeued element with the highest priority:", dequeued_task)
    print("Priority Queue after dequeue operation:", priority_queue.queue)

    # Example 4: Check if the priority queue is empty
    is_empty = priority_queue.is_empty()
    print("\nIs the priority queue empty?", is_empty)

    # Example 5: Check the size of the priority queue
    queue_size = priority_queue.size()
    print("\nSize of the priority queue:", queue_size)
