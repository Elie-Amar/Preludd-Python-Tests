class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding 
        self.previous = previous

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        for node in self.__iter__():
            return node.__str__()

    def __iter__(self):
        current = self.head
        while current:
            item_val = current.value
            current = current.succeeding
            yield item_val

    def unshift(self, new_value): # insert value at front 
        new_node = Node(new_value) 
 
        if self.head != None: # list empty isn't empty ? then
            new_node.succeeding = self.head # new head points to old head
            self.head.previous = new_node # previous old head points to new head
            self.head = new_node 

        else: # list empty, then
            self.head = new_node
            self.tail = new_node
        self.len += 1
    

    def push(self, new_value): # insert value at back
        new_node = Node(new_value)

        if self.tail != None: # list empty isn't empty ? then
            new_node.previous = self.tail
            self.tail.succeeding = new_node
            self.tail = new_node
              
        else: # list empty, then
            self.head = new_node 
            self.tail = new_node
        self.len += 1

    def shift(self): # remove value at front
        if self.head == None:
            print("List is empty, so it's like splash attack: no effect") #Magikarp 

        else:
            temp = self.head
            self.head = temp.succeeding # next node is now new head
            self.len -= 1
            if(self.len > 0):
                self.head.previous = None
            return temp.value
  
    def pop(self): # removes and returns the last element
        if self.tail == None:
            print("List is empty, so it's like splash attack: no effect") #Magikarp

        else:
            temp = self.tail
            self.tail = temp.previous # make second to last element the new tail
            self.len -= 1
            if(self.len > 0):
                self.tail.succeeding = None
            return temp.value

