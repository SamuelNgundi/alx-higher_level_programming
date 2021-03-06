#!/usr/bin/python3
"""Square with private instance atrribute"""


class Square:
    """Represents a square
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes class attribute
        """
        self.__size = size
