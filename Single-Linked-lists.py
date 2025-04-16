class SinglyNode: 

    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

#Defining four nodes using class

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

#Linking nodes to each other

Head.next = A 
A.next = B 
B.next = C 

#Function to display nodes individually

def showListNodes(Head):
    curr = Head
    while curr:
        print(curr)
        curr = curr.next

#Function to display all nodes with arrows

def displayLinkedList (Head):
    curr = Head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' => '.join(elements))

#Function that checks if val is in the list

def search(head, val):
    curr  = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False


    

    


    

