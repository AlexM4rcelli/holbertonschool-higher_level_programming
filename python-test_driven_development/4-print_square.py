#!/usr/bin/python3
"""This module prints a square with the character '#'"""


if __name__ == "__main__":
    def print_square(size):
        """
        Print a square with the character '#' of the given size.

        Args:
            size (int): The size (length) of the square.

        Raises:
            TypeError: If size is not an integer or is a float less than 0.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        for i in range(1, size + 1):
            for j in range(1, size + 1):
                print('#', end='')

                if j % size == 0 and j > 0:
                    print()
