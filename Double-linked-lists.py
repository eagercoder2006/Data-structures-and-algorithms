class DoublyNode:
    
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
        
head = DoublyNode(1)
B = DoublyNode(2)
C = DoublyNode(3)
tail = DoublyNode(7)

head.next = B
B.prev = head
B.next = C
C.prev = B
C.next = tail
tail.prev = C


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    
    print(" => ".join(elements))


def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail



def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return new_node, head



