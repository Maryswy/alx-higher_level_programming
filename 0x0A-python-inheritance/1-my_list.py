#!/usr/bin/python3

"""Module MyList"""


class MyList(list):
    """Print sorted list"""

    def print_sorted(self):
        """Print sorted list"""

        return print("{}".format(sorted(self)))
