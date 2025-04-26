class AddBinary:
    def __str__(self):
        return """
        67. Add Binary
        Given two binary strings a and b, return their sum as a binary string.
        """
    
    def addBinary(self, a: str, b: str) -> str:
        integer_to_binary = lambda integer : "{0:b}".format(integer)
        return integer_to_binary(int(a, 2) + int(b, 2))