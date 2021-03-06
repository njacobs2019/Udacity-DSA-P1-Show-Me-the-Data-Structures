class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    elements = set()

    # Add llist_1 to elements
    current = llist_1.head
    while current:
        elements.add(current.value)
        current = current.next

    # Add llist_2 to elements
    current = llist_2.head
    while current:
        elements.add(current.value)
        current = current.next

    # Create and fill the output linked list
    out = LinkedList()
    for elem in elements:
        out.append(elem)
    return out

def intersection(llist_1, llist_2):
    # Add llist_1 to elements1
    elements1 = set()
    current = llist_1.head
    while current:
        elements1.add(current.value)
        current = current.next

    # Add llist_2 to elements2
    elements2 = set()
    current = llist_2.head
    while current:
        if current.value in elements1:
            elements2.add(current.value)
        current = current.next

    # Create adn fill the output linked list
    out = LinkedList()
    for elem in elements2:
        out.append(elem)
    return out

if __name__ == '__main__':
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21,'a','!']
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print ("Union: {}".format(union(linked_list_1,linked_list_2)))
    print ("Intersection: {}".format(intersection(linked_list_1,linked_list_2)))
    print()

    # Output:
    # Union: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> ! -> a -> 21 -> 
    # Intersection: 4 -> 21 -> 6 -> 

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_4 = [1,7,8,9,11,21,1]

    for i in element_4:
        linked_list_4.append(i)

    print ("Union: {}".format(union(linked_list_3,linked_list_4)))
    print ("Intersection: {}".format(intersection(linked_list_3,linked_list_4)))
    print()

    # Output
    # Union: 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
    # Intersection: 

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    print ("Union: {}".format(union(linked_list_5,linked_list_6)))
    print ("Intersection: {}".format(intersection(linked_list_6,linked_list_5)))

    # Output:
    # Union: 
    # Intersection: 
