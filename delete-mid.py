# Assignment 2: Delete Middle
#
# Deletes the "middle" of a given linked list.
# By "middle", here we mean any node that is not
# the head and not the tail.
#
# This file has two slightly different implementations
# 1. delete(data)
#      searches for data in a linked list
#      and removes any reference to the node
#      containing that data
# 2. delete_middle(node)
#      "deletes" the data of the given node
#      by over-writing this node's data with
#      the next node's data. it then removes
#      and removes any reference to the next node.
#      this method preserves the surrounding structure
#      of the linked list that the node belongs to

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    # Function Definition: delete_middle(node)
    #
    # This is a member function, meaning it belongs to
    # the LinkedList class. You call this function
    # on a LinkedList object, see Usage.
    #
    # Usage:
    #   my_linked_list.delete("some data")
    def delete(self, data):
        # start at the beginning of the linked list
        temp = self.head

        # search through linked list from beginning to end
        while temp.next != None:
            # look ahead to check if the next node
            # has the data we are searching for
            if temp.next.data == data:
            # if true, then we want to delete that next node
                # ! delete node by changing the pointers !
                # we want to keep the current node
                # we want to delete the next node
                # we want to keep the node after next node
                temp.next = temp.next.next

            # iterate to the next node
            temp = temp.next

    def __repr__(self):
        s = ""
        temp = self.head
        while temp != None:
            s += temp.data
            s += " -> "
            temp = temp.next
        s += "|"
        return s

        



l = LinkedList()
l.append("a")
l.append("b")
l.append("c")
l.append("d")
l.append("e")


# Function Definition: delete_middle(node)
#
# Not a member function, meaning it does not belong to
# the LinkedList class. This function is defined at the
# top level, outside of the LinkedList class definition.
# You call this function standalone, see Usage.
#
# Usage:
#   delete_middle(some_node)
#   delete_middle(my_linked_list.head)
#   delete_middle(my_linked_list.head.next.next)
def delete_middle(node):
    # overwrite the data of the current node
    # with the data of the next node
    node.data = node.next.data

    # remove any references to the next node
    # by overwriting the current node's next pointer
    node.next = node.next.next




print(l)
print(l.head.next.next.data)
delete_middle(l.head.next.next)
print(l)



