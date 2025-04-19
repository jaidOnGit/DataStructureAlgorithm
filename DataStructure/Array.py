class Array:
    """
    Abstract Data Type: Array

    Arrays are linear data structures that store elements of the same type in contiguous memory locations.
    They allow constant-time access to elements via indices. Arrays support a variety of operations, including:
      - Traversal
      - Insertion
      - Deletion
      - Searching
      - Updating

    Properties:
      - Fixed Size: Predefined size during initialization.
      - Homogeneity: All elements are of the same type.
      - Contiguity: Elements stored in adjacent memory locations.

    Advantages:
      - Fast access to elements via indices.
      - Useful for storing data that needs to be retrieved quickly.

    Limitations:
      - Insertion and deletion can be costly (O(n)) due to the need for shifting elements.
      - Fixed size in many implementations (static arrays).

    Applications:
      - Used in scenarios requiring quick random access, such as matrices or static data storage.
      - Basis for other data structures like stacks, queues, and heaps.
    """

    def __init__(self, size):
        """
        Initialize an array with a specified size.
        All elements are initialized to None.

        :param size: The size of the array.
        """
        self.size = size
        self.array = [None] * size

    def traverse(self):
        """
        Traverse and display all elements in the array.

        :return: None
        """
        print("Array elements:")
        for i in range(self.size):
            print(f"Index {i}: {self.array[i]}")

    def insert(self, index, value):
        """
        Insert a value at the specified index.

        :param index: The index at which to insert the value.
        :param value: The value to insert.
        :return: None
        """
        if index < 0 or index >= self.size:
            print("Error: Index out of bounds")
        else:
            self.array[index] = value

    def delete(self, index):
        """
        Delete an element at the specified index by setting it to None.

        :param index: The index of the element to delete.
        :return: None
        """
        if index < 0 or index >= self.size:
            print("Error: Index out of bounds")
        else:
            self.array[index] = None

    def search(self, value):
        """
        Search for a value in the array and return its index.

        :param value: The value to search for.
        :return: The index of the value if found; otherwise, -1.
        """
        for i in range(self.size):
            if self.array[i] == value:
                return f"Value {value} found at index {i}"
        return "Value not found"

    def update(self, index, value):
        """
        Update the value at a specified index with a new value.

        :param index: The index of the element to update.
        :param value: The new value to set.
        :return: None
        """
        if index < 0 or index >= self.size:
            print("Error: Index out of bounds")
        else:
            self.array[index] = value

    def reverse(self):
        """
        Reverse the array in place.

        :return: reversed array
        """
        reversed_array = self.array[::-1]
        return reversed_array 

    def merge(self, other_array):
        """
        Merge the current array with another array.

        :param other_array: The array to merge with the current array.
        :return: A new array with merged elements.
        """
        merged = self.array + other_array.array
        return 
    
class DynamicArray:
    """
    Abstract Data Type: Dynamic Array

    A dynamic array is a resizable array that can automatically grow or shrink during runtime.
    This class provides basic operations such as insertion, deletion, resizing, and traversal.

    Applications:
      - Used in dynamic data storage (e.g., lists, buffers, or stacks).
      - Basis for implementing higher-level structures like queues or vectors.
    
    Limitations:
      - Insertions and deletions require shifting elements.
      - Resizing can have significant overhead.

    Properties:
      - Resizable: Automatically increases capacity when needed.
      - Contiguous memory allocation for fast access.
    """

    def __init__(self):
        """
        Initialize an empty dynamic array.
        """
        self.array = [None] * 2  # Initial capacity of 2
        self.size = 0
        self.capacity = 2

    def _resize(self):
        """
        Resize the array when the size exceeds capacity.
        """
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert(self, value):
        """
        Add an element to the end of the dynamic array.

        :param value: The value to insert.
        :return: None
        """
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def delete(self, index):
        """
        Remove an element at the specified index.

        :param index: The index of the element to delete.
        :return: None
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def search(self, value):
        """
        Search for a value in the array.

        :param value: The value to search for.
        :return: The index of the value if found; otherwise, -1.
        """
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def traverse(self):
        """
        Traverse and display all elements in the dynamic array.

        :return: None
        """
        print("Dynamic Array elements:")
        for i in range(self.size):
            print(self.array[i], end=" ")
        print()

    def get(self, index):
        """
        Retrieve the element at the specified index.

        :param index: The index of the element.
        :return: The element at the given index.
        :raises IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]


def test_array():
    # Instantiate the Array class
    array_instance = Array(size=5)  # Create an array of size 5

    # Example 1: Traversing the array (currently empty)
    array_instance.traverse()

    # Example 2: Inserting values
    array_instance.insert(0, 10)  # Insert 10 at index 0
    array_instance.insert(2, 30)  # Insert 30 at index 2
    array_instance.insert(4, 50)  # Insert 50 at index 4

    # Display the array after insertion
    print("\nAfter insertion:")
    array_instance.traverse()

    # Example 3: Searching for a value
    search_result = array_instance.search(30)  # Search for value 30
    print("\nSearch Result:", search_result)

    # Example 4: Deleting a value
    array_instance.delete(2)  # Delete the value at index 2
    print("\nAfter deletion:")
    array_instance.traverse()

    # Example 5: Updating a value
    array_instance.update(1, 20)  # Update value at index 1 to 20
    print("\nAfter update:")
    array_instance.traverse()

    # Example 6: Reversing the array
    array_instance.reverse()
    print("\nAfter reversing the array:")
    array_instance.traverse()

    # Example 7: Merging with another array
    other_array = Array(size=3)  # Create another array
    other_array.insert(0, 60)
    other_array.insert(1, 70)
    other_array.insert(2, 80)

    merged_array = array_instance.merge(other_array)
    print("\nMerged Array:", merged_array)

def test_dynamic_array():

    # Instantiate the DynamicArray class
    dynamic_array = DynamicArray()

    # Example 1: Insert elements into the dynamic array
    dynamic_array.insert(10)
    dynamic_array.insert(20)
    dynamic_array.insert(30)  # Triggers resizing
    dynamic_array.insert(40)
    print("\nDynamic Array after insertion:")
    dynamic_array.traverse()

    # Example 2: Retrieve an element by index
    element = dynamic_array.get(1)
    print("\nElement at index 1:", element)

    # Example 3: Delete an element by index
    dynamic_array.delete(2)
    print("\nDynamic Array after deletion at index 2:")
    dynamic_array.traverse()

    # Example 4: Search for an element
    index = dynamic_array.search(20)
    print("\nIndex of element 20:", index)

    # Example 5: Check resizing behavior (capacity doubling)
    print("\nArray capacity after resizing:", dynamic_array.capacity)
