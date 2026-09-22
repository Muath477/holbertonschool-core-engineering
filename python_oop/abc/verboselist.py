#!/usr/bin/env python3
"""Define a VerboseList that announces every mutation it makes."""


class VerboseList(list):
    """A list subclass that announces every mutation it makes."""

    def append(self, item):
        """Append item to the list and announce it.

        Args:
            item: The item to append.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with iterable and announce how many items.

        Args:
            iterable: The items to extend the list with.
        """
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Announce and remove the first occurrence of item.

        Args:
            item: The item to remove.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Announce and remove the item at index (default last).

        Args:
            index (int): The index of the item to pop.

        Returns:
            The popped item.
        """
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
