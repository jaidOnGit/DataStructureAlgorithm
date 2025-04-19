class LinkedListNode:
    """
    Node Representation:
    Each node consists of data and a pointer to the next node.
    """
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Pointer to the next node


class LinkedList:
    """
    Abstract Data Type: Linked List

    Linked lists are a linear data structure where elements, called nodes, are connected via pointers.
    This class provides basic operations like insertion, deletion, traversal, searching, and reversal.

    Properties:
      - Dynamic size (can grow or shrink at runtime).
      - Nodes stored in non-contiguous memory locations.
      - Efficient insertions and deletions compared to arrays.

    Applications:
      - Used to implement data structures like stacks, queues, and adjacency lists for graphs.
      - Suitable for dynamic memory allocation and real-time applications.

    Limitations:
      - Sequential access only (no random access like arrays).
      - Increased memory usage due to pointers.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None  # Pointer to the first node

    def traverse(self):
        """
        Traverse and display all nodes in the linked list.

        :return: None
        """
        current = self.head
        print("Linked List elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the linked list.

        :param data: The data to insert.
        :return: None
        """
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the linked list.

        :param data: The data to insert.
        :return: None
        """
        new_node = LinkedListNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        """
        Delete the first node that contains the given key.

        :param key: The value to delete.
        :return: None
        """
        current = self.head

        # If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    def reverse(self):
        """
        Reverse the linked list in place.

        :return: None
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

def test_linkedlist():
    # Instantiate the LinkedList class
    linked_list = LinkedList()

    # Observation 1: Insert nodes at the beginning
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(30)
    print("\nAfter inserting nodes at the beginning:")
    linked_list.traverse()

    # Observation 2: Insert nodes at the end
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)
    print("\nAfter inserting nodes at the end:")
    linked_list.traverse()

    # Observation 3: Delete a node by value
    linked_list.delete_node(20)
    print("\nAfter deleting node with value 20:")
    linked_list.traverse()

    # Observation 4: Reverse the linked list
    linked_list.reverse()
    print("\nAfter reversing the linked list:")
    linked_list.traverse()

