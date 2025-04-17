class SinglyNode: 

    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

#Defining four nodes using class

Head = SinglyNode(0)
A = SinglyNode(7)
B = SinglyNode(11)
C = SinglyNode(20)

#Linking nodes to each other

Head.next = A 
A.next = B 
B.next = C 

def reverse (node):
    if not node:
        return
    
    reverse(node.next)
    print(node)

reverse(Head)
