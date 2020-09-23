class Stack_imp:
    def __init__(self,capacity):
        self.top =-1
        self.capacity = capacity
        self.array = []
        self.output =[]
        self.precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}


    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

    def Peek(self):
        return self.array[-1]

    def Pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"

    def Push(self,data):
        self.top+=1
        self.array.append(data)


if __name__=='__main__':
    cap = int(input("Enter capacity of stack :"))
    S = Stack_imp(cap)
    c=0
    while(c!=5):
        print("--Stack --"
              "\n1.Push"
              "\n2.Pop"
              "\n3.Peek"
              "\n4.Is empty"
              "\n5.Exit")
        c=int(input("Enter Choice : "))
        if c==1:
            data =int(input("Enter data : "))
            S.Push(data)
        elif c==2:
            print(S.Pop())
        elif c==3:
            print(S.Peek())
        elif c==4:
            print(S.isEmpty())
        elif c==5:
            break
        else:
            print("Retry wrong input :")




