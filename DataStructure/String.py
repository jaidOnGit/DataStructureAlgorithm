class StringManipulator:
    """
    Abstract Data Type: String

    Strings are linear sequences of characters used for text manipulation and representation.
    They are immutable in many programming languages, meaning their contents cannot be
    changed after creation. The String ADT supports operations such as traversal, reversal,
    searching, concatenation, and pattern matching without exposing implementation details.

    Properties:
      - Sequence of characters.
      - Immutable: Modifications result in the creation of a new string.
      - Indexable and sliceable for efficient character and substring access.
      - Unicode support for multilingual and symbolic text handling.

    Advantages:
      - Simplifies text manipulation tasks.
      - Immutability ensures thread safety in concurrent environments.

    Limitations:
      - Memory overhead due to immutability (e.g., new string created during concatenation).
      - Advanced manipulations like regular expressions may require external libraries.

    Applications:
      - Text processing and formatting (e.g., documents, messages).
      - Searching and pattern matching (e.g., substring finding, regex).
      - Serialization/deserialization of structured data.
      - Encoding/decoding tasks (e.g., URL encoding, Base64).

    This class provides methods to perform common operations on strings, such as traversal,
    reversal, searching, palindrome checking, concatenation, and basic pattern matching.
    """

    def __init__(self, input_string):
        """
        Initialize with an input string.

        :param input_string: The string to be manipulated.
        """
        self.string = input_string

    def traverse(self):
        """
        Traverse and display characters in the string.

        :return: None
        """
        print("Traversing the string:")
        for index, char in enumerate(self.string):
            print(f"Character at index {index}: {char}")

    def reverse(self):
        """
        Reverse the string and return it.

        :return: The reversed string.
        """
        return self.string[::-1]

    def search_substring(self, substring):
        """
        Search for a substring in the string.

        :param substring: The substring to search for.
        :return: The start index of the substring if found; otherwise, -1.
        """
        for i in range(len(self.string) - len(substring) + 1):
            if self.string[i:i+len(substring)] == substring:
                return f"Substring '{substring}' found at index {i}"
        return f"Substring '{substring}' not found"

    def is_palindrome(self):
        """
        Check if the string is a palindrome.

        :return: True if the string is a palindrome; otherwise, False.
        """
        return self.string == self.reverse()

    def concatenate(self, other_string):
        """
        Concatenate another string to the current string.

        :param other_string: The string to concatenate.
        :return: The concatenated string.
        """
        return self.string + other_string

    def pattern_match(self, pattern):
        """
        Match a basic pattern in the string.

        :param pattern: The pattern to match.
        :return: True if the pattern exists in the string; otherwise, False.
        """
        return pattern in self.string

    def find_frequency(self, char):
        """
        Find the frequency of a character in the string.

        :param char: The character whose frequency to find.
        :return: The frequency of the character in the string.
        """
        return self.string.count(char)

    def remove_character(self, index):
        """
        Remove a character from the string at a specified index.

        :param index: The index of the character to remove.
        :return: The string after removal.
        """
        if index < 0 or index >= len(self.string):
            return "Error: Index out of bounds"
        return self.string[:index] + self.string[index+1:]

    def advanced_pattern_match(self, pattern):
        """
        Perform advanced pattern matching (e.g., regex-like patterns) in the string.

        :param pattern: The pattern to match.
        :return: True if the pattern matches; otherwise, False.
        """
        import re
        return bool(re.search(pattern, self.string))

def test_string():
    # Instantiate the class with an input string
    string_instance = StringManipulator("madam")

    # Example 1: Traverse the string
    string_instance.traverse()

    # Example 2: Reverse the string
    reversed_string = string_instance.reverse()
    print("\nReversed String:", reversed_string)

    # Example 3: Search for a substring
    search_result = string_instance.search_substring("dam")
    print("\nSearch Result:", search_result)

    # Example 4: Check if the string is a palindrome
    is_palindrome_result = string_instance.is_palindrome()
    print("\nIs Palindrome:", is_palindrome_result)

    # Example 5: Concatenate another string
    concatenated_string = string_instance.concatenate(" is a word!")
    print("\nConcatenated String:", concatenated_string)

    # Example 6: Pattern matching
    pattern_match_result = string_instance.pattern_match("mad")
    print("\nPattern Match Result:", pattern_match_result)

    # Example 7: Find frequency of a character
    frequency = string_instance.find_frequency("a")
    print("\nFrequency of 'a':", frequency)

    # Example 8: Remove a character at a specified index
    removed_character_string = string_instance.remove_character(2)  # Removes character at index 2
    print("\nString after removing character:", removed_character_string)

    # Example 9: Perform advanced pattern matching (regex-like)
    advanced_pattern_result = string_instance.advanced_pattern