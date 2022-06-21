#!/usr/bin/python3
"""Class that defines a square and finds the area"""


class Square:
    """Public instance method self that returns current square area.
    """
    def __init__(self, size=0):
        """Initializes class attributes
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Computes and returns current square area
        """
        return self.__size ** 2
