
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ListClass:
    def __init__(self):
        self.head = None

    '''data add into linked list'''
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

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last=last.next
        last.next = new_node

    ''' delete node '''

    def delete_head(self):
        if(self.head is not None):
            temp = self.head.next
            self.head.next = None
            self.head = temp


    def delete_node(self,key):
        temp = self.head
        # first to initilize pointed node as none value
        if (temp is not None):
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp==None:
            return
        prev.next = temp.next
        temp = None

    def delete_last(self):
        if self.head is not None:
            temp = self.head
            while(temp.next.next):
                temp = temp.next
            temp.next=None

    ''' print data of linked list '''

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data , end=' ')
            temp = temp.next

    def printReverse(self,head):
        temp = head
        if temp:
            self.printReverse(temp.next)
            print(temp.data,end=' ')
        else:
            return head

    ''' length of linked list'''

    def List_length(self):
        c=0
        if self.head is not None:
            c=1
            temp = self.head
            while(temp.next):
                c+=1
                temp=temp.next
        return c

    '''search and check data '''

    def check_data(self,h,data):
        if h is None:
            return False
        if h.data==data:
            return True
        else:
            return self.check_data(h.next,data)

    def search_data(self,data):
        if self.head is None:
            return -1
        if self.head.data==data:
            return 0
        count = 0
        temp = self.head
        while(temp):
            if temp.data == data:
                return count
            count+=1
            temp = temp.next
        return -1

    ''' remove duplicates from linked list '''
    def remove_duplicates(self):
        temp = self.head
        while(temp.next):
            if temp.data == temp.next.data:
                l=temp.next.next
                temp.next =None
                temp.next = l
            else:
                temp = temp.next




if __name__=='__main__':
    llist = ListClass()
    c=int()
    n=0
    while(c!=7):
        print("--menu--"
              "\n1.Add Data"
              "\n2.Delete Data"
              "\n3.Print Data"
              "\n4.Length of list"
              "\n5.Check & Search"
              "\n6.Remove duplicates"
              "\n7.Exit")
        c=int(input("Choose Option :"))
        if c==1:
            i=0
            while(i!=4):
                print("1.Add at head "
                      "\n2.Add at last"
                      "\n3.Add after node"
                      "\n4.Insert group of data "
                      "\n5.Back")
                i=int(input("Enter choice :"))
                if i==1:
                    data = int(input("Enter data :"))
                    llist.push(data)
                elif i==2:
                    data = int(input("Enter data : "))
                    llist.append(data)
                elif i==3:
                    data = int(input("Enter data :"))
                    prev_nodeData = int(input("enter data of previous node : "))
                    previous = None
                    temp = llist.head
                    while (temp):
                        if temp.data == prev_nodeData:
                            previous = temp
                            break
                        temp = temp.next
                    llist.insertAfter(previous, data)
                elif i==4:
                    datalist = list(map(int,input().split()))
                    for i in datalist:
                        llist.append(i)
                elif i==5:
                    break
                else:
                    print("Retry ! invalid input")

        elif c==2:
            i=0
            while(i!=4):
                print("1.Delete head node"
                      "\n2.Delete last node"
                      "\n3.Delete Given node"
                      "\n4.Back")
                i = int(input("Choose option :"))
                if i==1:
                    llist.delete_head()
                elif i==2:
                    llist.delete_last()
                elif i==3:
                    data = int(input("Enter node data :"))
                    llist.delete_node(data)
                elif i==4:
                    break
                else:
                    print("Retry ! invalid input")

        elif c==3:
            i=0
            while(i!=3):
                print("\n1.In order print"
                      "\n2.Reverse print"
                      "\n3.back")
                i=int(input("Enter choice : "))
                if i==1:
                    llist.printList()
                elif i==2:
                    llist.printReverse(llist.head)
                elif i==3:
                    break
                else:
                    print("Invalid input ")
        elif c==4:
            print("Length :",llist.List_length())
        elif c==5:
            i=0
            while(i!=4):
                print("1.Check if data in list"
                      "\n2.Search element position"
                      "\n3.back")
                i=int(input("Enter Choice :"))
                if i==1:
                    data = int(input("Enter data to check : "))
                    res = llist.check_data(llist.head,data)
                    if res==True:
                        print("Data is present in list ")
                    else:
                        print("Data not Present")

                elif i==2:
                    data =int(input("Enter data :"))
                    pos =  llist.search_data(data)
                    if pos==-1:
                        print("no data found")
                    else:
                        print(data ," is on index", pos)

                elif i==3:
                    break
                else:
                    print("Invalid output")
        elif c==6:
            i=0
            while(i!=3):
                print("\n1.Remove duplicates from sorted array"
                      "\n2.Remove duplicates from unsorted array "
                      "\n3.Back")
                i=int(input("Enter choice :"))
                if i ==1:
                    llist.remove_duplicates()
                elif i==2:
                    pass
                elif i==3:
                    break
                else:
                    print("invalid input")
        elif c==7:
            break
        else:
            print("invalid output ")
















