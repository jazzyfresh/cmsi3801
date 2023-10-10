
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

    def delete(self, data):
        # start at the beginning of the linked list
        temp = self.head

        # search through linked list from beginning to end
        while temp.next != None:
            # look ahead to check if the next node
            # has the data we are searching for
            # if so, then we want to delete that next node
            if temp.next.data == data:
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


def delete_middle(node):
    # delete the node that you're given 
    # from the linked list that its a part of

    temp = node
    while temp != None:
        temp.data = temp.next.data
        if temp.next.next == None:
            temp.next = None
        temp = temp.next

    return node



print(l)
print(l.head.next.next.data)
delete_middle(l.head.next.next)
print(l)



