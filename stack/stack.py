"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# Like a set of plates
# Can't get to bottom unless you go through the top
# Last In First Out (LIFO)

# Removing items from the front of a linked list is much easier because moving the head pointer to the next node
# is done in constant time
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()


# LIFO is generally ok for lists

# When adding elements to the back of the list we have to copy the list and add those elements
# meaning we have to touch every element in the list just to add to the back
# If we have data in the front and we delete something we have to move every item in that list over


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)
#
#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             popped = self.storage.pop()
#             self.size = len(self.storage)
#             return popped

# Sean's solution

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return len(self.storage)
#
#     def push(self, value):
#         # self.storage.insert(0, value) # O(n)
#         self.storage.append(value) # O(1)
#
#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop() # O(1)
#         return None

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)
#
#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.remove_tail()
#         return None


# In arrays (lists) elements are contiguous in memory (arranged one after another)

# Pros: Easier to find where everything is. We know starting from the first index and the length of the array,
# we can jump n times to whichever value we need. eg. from 1 if len is 5, and we need 3 just jump twice to get to 3.

# Cons: If memory is taken up next to our array and we want to add data we won't have contiguous chunks of memory to
# add our data. (disk fragmentation)
# Finding a new contiguous chunk of memory and moving all the elements over is expensive, especially when compared
# adding an element when there already is enough space

# Removing from the front of array arr.pop(0)
# removes first index but then each element has to move back one spot. can't have empty space in array, only at the end
# of an array


# Array is what is call Static Data structure because the memory is static once it is allocated, the memory can't be
# shrink or extend once it is allocated. To increase the memory size the whole array need to be copy to a new memory
# larger this is due to the contiguous nature of array all elements has to be contiguous this why it is possible to
# index to array and get out an element.


# In a linked list elements (nodes) are NOT contiguous in memory

# No need to pack them contiguously

# remove head is O(1) constant time

