# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/28/2023
# Description: Write a LinkedList class that has recursive implementations


# LinkedList.py

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A linked list implementation of the List ADT 
    """
    def __init__(self):
        self._head = None
        self._length = 0


    def add(self, val):
        """Adds a node containing val to the end of the linked list"""
        if self._head is None:      # If the list is empty
            self._head = Node(val)
            self._length += 1
        else:
            self.rec_add(self._head, val)
            self._length += 1

    def rec_add(self, current, val):
        """Recursive helper method for add"""
        if current.next is None:
            current.next = Node(val)
        else:
            self.rec_add(current.next, val)

    def remove(self, val):
        """Removes the node containing val from the linked list"""
        self._head = self.rec_remove(self._head, val)
        self._length -= 1

    def rec_remove(self, current, val):
        """Recursive helper method for remove"""
        if current is None:
            return None

        if current.data == val:
            return current.next

        current.next = self.rec_remove(current.next, val)
        return current

    def contains(self, val):
        """Returns True if the linked list contains the given value, False otherwise"""
        return self.rec_contains(self._head, val)

    def rec_contains(self, current, val):
        """Recursive helper method for contains"""
        if current is None:
            return False

        if current.data == val:
            return True

        return self.rec_contains(current.next, val)

    def insert(self, val, index):
        """Inserts a node containing val at the specified index"""

        if index < 0:        # Convert negative index
            index += self._length
            self._head = self.rec_insert(self._head, val, index)
    


        elif index < 0 or index > self._length:
            print('index out of range.')


        else:
            self._head = self.rec_insert(self._head, val, index)
            


    def rec_insert(self, current, val, index):
        """Recursive helper method for insert"""
        if index == 0:
            new_node = Node(val)
            new_node.next = current
            self._length += 1
            return new_node

        if current is None:
            self._length += 1
            return Node(val)

        current.next = self.rec_insert(current.next, val, index - 1)
        return current

    def reverse(self):
        """Reverses the linked list in place"""
        self._head = self.rec_reverse(self._head)

    def rec_reverse(self, current):
        """Recursive helper method for reverse"""
        if current is None or current.next is None:
            return current

        rest = self.rec_reverse(current.next)
        current.next.next = current
        current.next = None
        return rest

    def to_plain_list(self):
        """Returns a regular Python list with the same values and order as the linked list"""
        return self.rec_to_plain_list(self._head)

    def rec_to_plain_list(self, current):
        """Recursive helper method for to_plain_list"""
        if current is None:
            return []
        return [current.data] + self.rec_to_plain_list(current.next)

    def get_head(self):
        """Returns the first Node object in the list"""
        return self._head

