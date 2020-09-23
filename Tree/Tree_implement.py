class Tree_implement:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.c = 1

    def Nodes_in_tree(self):
        return self.c

    def printInorder(self,root):
        if root:
            self.printInorder(root.left)
            print(root.data,end=' ')
            self.printInorder(root.right)

    def printPostorder(self,root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print(root.data,end=' ')


    def printPreorder(self,root):
        if root:
            print(root.data,end=' ')
            self.printPreorder(root.left)
            self.printPreorder(root.right)

    def AddData(self,root):
        temp = root
        while(1):
            print("Add",temp.data,"'s \n1.Left \n2.Right\n3.exit")
            c=int(input("Enter choice :"))
            if c==1:
                if temp.left==None:
                    data = int(input("Enter data :"))
                    temp.left = Tree_implement(data)
                    self.c+=1
                    print("Your Tree now :",self.printInorder(root))
                temp = temp.left

            elif c==2:
                if temp.right==None:
                    data=int(input("Enter data :"))
                    temp.right = Tree_implement(data)
                    self.c+=1
                    print("Your Tree now :", self.printInorder(root))
                temp = temp.right
            elif c==3:
                break
            else:
                print("Choose correct option ")



if __name__=='__main__':
    R = int(input("Enter Root Node : "))
    T = Tree_implement(R)
    c=0
    while(c!=5):
        print("\n1.PrintTree"
              "\n2.Add data"
              "\n3.Nodes in tree"
              "\n5.Exit\n")
        c=int(input("Enter choice : "))
        if c==1:
            i = 0
            while (i != 4):
                print("1.Inorder print"
                      "\n2.Postorder print"
                      "\n3.Preorder print"
                      "\n4.Back")
                i = int(input("Enter Choice :"))
                if i == 1:
                    T.printInorder(T)
                    print("\n")
                elif i==2:
                    T.printPostorder(T)
                    print("\n")
                elif i==3:
                    T.printPreorder(T)
                    print("\n")
                elif i==4:
                    break
                else:
                    print("Invalid input !")

        elif c==2:
            T.AddData(T)

        elif c==3:
            c=0
            print("Nodes in tree : ",T.Nodes_in_tree())
        elif c==5:
            break
        else:
            print("Wrong input ")

