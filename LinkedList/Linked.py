class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ListClass:
    def __init__(self):
        self.head = None
    # push function insert data at starting index
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,pnode,ndata):
        if pnode is None:
            print("must be linked previous link")
            return
        new_node = Node(ndata)
        new_node.next = pnode.next
        pnode.next = new_node
    # data will be insert at the last
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last=last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = ListClass()
    llist.append(6)
    llist.append(1)
    llist.append(4)
    llist.push(3)
    llist.push(10)
    llist.printList()








