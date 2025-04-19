class Stack:
    """
    Abstract Data Type: Stack

    A stack is a linear data structure that operates on the LIFO (Last-In-First-Out) principle.
    It allows operations like push, pop, peek, and checking if the stack is empty.

    Applications:
      - Used in function call management, recursion, and expression evaluation.
      - Ideal for scenarios requiring temporary storage with LIFO access.

    Limitations:
      - Access limited to the top element.
      - Fixed size for static implementations.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.stack = []

    def push(self, item):
        """
        Push an element onto the stack.

        :param item: The element to add.
        :return: None
        """
        self.stack.append(item)

    def pop(self):
        """
        Pop the top element from the stack.

        :return: The popped element.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Peek at the top element of the stack without removing it.

        :return: The top element.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Get the number of elements in the stack.

        :return: The size of the stack.
        """
        return len(self.stack)

def test_stack():
    # Instantiate the Stack class
    stack = Stack()

    # Example 1: Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("\nStack after pushing elements:")
    print(stack.stack)  # Current state of the stack

    # Example 2: Peek at the top element
    top_element = stack.peek()
    print("\nTop element of the stack (peek):", top_element)

    # Example 3: Pop an element from the stack
    popped_element = stack.pop()
    print("\nPopped element:", popped_element)
    print("Stack after popping an element:")
    print(stack.stack)

    # Example 4: Check if the stack is empty
    is_empty = stack.is_empty()
    print("\nIs the stack empty?", is_empty)

    # Example 5: Get the size of the stack
    stack_size = stack.size()
    print("\nSize of the stack:", stack_size)
