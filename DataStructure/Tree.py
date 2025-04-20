class TreeNode:
    """
    Node Representation:
    Each node consists of data and references to its left and right children.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Abstract Data Type: Binary Tree

    A tree is a hierarchical data structure consisting of nodes. Each node in a binary tree has a maximum
    of two children, referred to as left and right children. This class provides methods for traversal,
    insertion, searching, and calculating the height of the tree.

    Applications:
      - Represent hierarchical data such as file systems and organizational charts.
      - Efficient data searching and sorting (e.g., Binary Search Tree).
    
    Limitations:
      - Can be memory-intensive if the tree is unbalanced.
      - Traversal or search operations can become inefficient in unbalanced trees.
    """
    def __init__(self, root_data):
        """
        Initialize the binary tree with a root node.

        :param root_data: The data of the root node.
        """
        self.root = TreeNode(root_data)

    def insert_left(self, parent_node, data):
        """
        Insert a node to the left of a given parent node.

        :param parent_node: The parent node.
        :param data: The data for the new node.
        :return: None
        """
        parent_node.left = TreeNode(data)

    def insert_right(self, parent_node, data):
        """
        Insert a node to the right of a given parent node.

        :param parent_node: The parent node.
        :param data: The data for the new node.
        :return: None
        """
        parent_node.right = TreeNode(data)

    def preorder_traversal(self, node):
        """
        Perform a preorder traversal of the tree.

        :param node: The starting node for traversal.
        :return: List of nodes in preorder.
        """
        if node:
            return [node.data] + self.preorder_traversal(node.left) + self.preorder_traversal(node.right)
        return []

    def inorder_traversal(self, node):
        """
        Perform an inorder traversal of the tree.

        :param node: The starting node for traversal.
        :return: List of nodes in inorder.
        """
        if node:
            return self.inorder_traversal(node.left) + [node.data] + self.inorder_traversal(node.right)
        return []

    def postorder_traversal(self, node):
        """
        Perform a postorder traversal of the tree.

        :param node: The starting node for traversal.
        :return: List of nodes in postorder.
        """
        if node:
            return self.postorder_traversal(node.left) + self.postorder_traversal(node.right) + [node.data]
        return []

    def calculate_height(self, node):
        """
        Calculate the height of the tree.

        :param node: The starting node for height calculation.
        :return: The height of the tree.
        """
        if node is None:
            return -1
        return 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))

def test_tree():
    # Instantiate the BinaryTree class with a root node
    binary_tree = BinaryTree("A")

    # Insert nodes to form the tree structure
    binary_tree.insert_left(binary_tree.root, "B")
    binary_tree.insert_right(binary_tree.root, "C")
    binary_tree.insert_left(binary_tree.root.left, "D")
    binary_tree.insert_right(binary_tree.root.left, "E")
    binary_tree.insert_left(binary_tree.root.right, "F")
    binary_tree.insert_right(binary_tree.root.right, "G")

    # Example 1: Preorder traversal
    print("\nPreorder Traversal:", binary_tree.preorder_traversal(binary_tree.root))

    # Example 2: Inorder traversal
    print("\nInorder Traversal:", binary_tree.inorder_traversal(binary_tree.root))

    # Example 3: Postorder traversal
    print("\nPostorder Traversal:", binary_tree.postorder_traversal(binary_tree.root))

    # Example 4: Calculate height of the tree
    print("\nHeight of the Tree:", binary_tree.calculate_height(binary_tree.root))
