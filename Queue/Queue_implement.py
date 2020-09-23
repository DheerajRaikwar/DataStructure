class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear =None

    def isEmpty(self):
        return self.front==None

    def Enqueue(self,data):
        temp = Node(data)
        if self.rear==None:
            self.front=self.rear=temp
            return
        self.rear.next = temp
        self.rear = temp

    def Dequeue(self):
        if self.isEmpty():
            return
        temp= self.front
        self.front = temp.next
        if(self.front==None):
            self.rear = None

    def PrintQueue(self):
        f= self.front
        if self.isEmpty():
            print("Queue is empty")
            return

        if self.front==self.rear:
            print(self.front.data)
        while(f):
            print(f.data,end=' ')
            f = f.next
        print("\n")





if __name__=='__main__':
    Q = Queue()
    c=0
    while(c!=5):
        print("1.Enqueue"
              "\n2.Dequeue"
              "\n3.isEmpty"
              "\n4.PrintQueue"
              "\n5.Exit\n")
        c=int(input("\nEnter Choice : "))
        if c==1:
            data = int(input("Enter data :"))
            Q.Enqueue(data)
        elif c==2:
            Q.Dequeue()

        elif c==3:
            y=Q.isEmpty()
            if y==True:
                print("Queue is empty")
            else:
                print("Queue not empty")

        elif c==4:
            Q.PrintQueue()
        elif c==5:
            break
        else:
            print("Enter valid input")

