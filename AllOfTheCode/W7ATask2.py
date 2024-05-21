class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval  # Initialize the data value of the node
        self.nextval = None     # Initialize the reference to the next node as None

class SLinkedList:
    def __init__(self):
        self.headval = None     # Initialize the head of the linked list as None
        self.last = None        # Initialize the last node of the linked list as None

    # Method to print the elements of the linked list
    def listprint(self):
        printval = self.headval  # Start from the head of the linked list
        while printval is not None:
            print(printval.dataval)  # Print the data value of the current node
            printval = printval.nextval  # Move to the next node

    # Method to insert a new node at the beginning of the linked list
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)  # Create a new node with the given data 
        NewNode.nextval = self.headval  # Set the next reference of the new node to the current head 
        self.headval = NewNode  # Update the head reference to point to the new node 

    # Method to insert a new node at the end of the linked list
    def AtEnd(self, newdata):
        NewNode = Node(newdata)  # Create a new node with the given data
        if self.headval is None:  # If the linked list is empty
            # Set the new node as both the head and the last node
            self.headval = self.last = NewNode
            return
        last = self.headval  # Start from the head of the linked list
        while(last.nextval):  # Traverse the linked list until the last node
            last = last.nextval
        last.nextval = NewNode  # Set the next node of the last node as the new node
        self.last = NewNode     # Update the last node to be the new node

    # Method to insert a new node after a specific node in the linked list
    def Insert(self,val_before,newdata):
        if val_before is None:  # If the given node is None
            print("No node to insert after")  # Print an error message
            return
        else:
            new_node = Node(newdata)  # Create a new node with the given data
            # Insert the new node after the specified node
            new_node.nextval = val_before.nextval
            val_before.nextval = new_node
            # Update pointers and adjust the last node if necessary
            if new_node.nextval is not None:
                new_node.nextval.val_before = new_node
            if self.headval is None:
                self.headval = self.last = new_node
                new_node.val_before = new_node.nextval = None
            elif self.last == val_before:
                self.last = new_node


list = SLinkedList()  # Create a new singly linked list object
list.headval = Node("Mon")  # Set the head of the linked list to a new node with "Mon" as data

# Create additional nodes and link them to form a linked list
e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

list.Insert(e2,"Wed")  # Insert "Wed" after "Tue"
list.AtEnd("Sun")      # Insert "Sun" at the end of the linked list

list.listprint()       # Print the elements of the linked list