class Queue:
    """
    Abstract Data Type: Queue

    A queue is a linear data structure that operates on the FIFO (First-In-First-Out) principle.
    It allows operations like enqueue, dequeue, peek, and checking if the queue is empty.

    Applications:
      - Task scheduling in operating systems, BFS in graph traversal.
      - Useful in managing ordered workflows like customer service lines.
    
    Limitations:
      - Access is limited to the front and rear.
      - Fixed size for static implementations.
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.queue = []

    def enqueue(self, item):
        """
        Add an element to the rear of the queue.

        :param item: The element to add.
        :return: None
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return the front element from the queue.

        :return: The dequeued element.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        """
        Peek at the front element of the queue without removing it.

        :return: The front element.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def is_empty(self):
        """
        Check if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Get the number of elements in the queue.

        :return: The size of the queue.
        """
        return len(self.queue)

def test_queue():
    # Instantiate the Queue class
    queue = Queue()

    # Example 1: Enqueue elements into the queue
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("\nQueue after enqueue operations:")
    print(queue.queue)  # Current state of the queue

    # Example 2: Peek at the front element
    front_element = queue.peek()
    print("\nFront element of the queue (peek):", front_element)

    # Example 3: Dequeue an element from the queue
    dequeued_element = queue.dequeue()
    print("\nDequeued element:", dequeued_element)
    print("Queue after dequeue operation:")
    print(queue.queue)

    # Example 4: Check if the queue is empty
    is_empty = queue.is_empty()
    print("\nIs the queue empty?", is_empty)

    # Example 5: Get the size of the queue
    queue_size = queue.size()
    print("\nSize of the queue:", queue_size)
