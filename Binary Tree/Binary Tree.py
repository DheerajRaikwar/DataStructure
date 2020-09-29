class binary_tree:
    def __init__(self,data):
        self.key = data
        self.right = None
        self.left = None
        self.c=1

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

    def insert(self,temp,key):
        self.c+=1
        if not temp:
            root = binary_tree(key)
            return
        q = []
        q.append(temp)
        while(len(q)):
            temp = q[0]
            q.pop(0)

            if (not temp.left):
                temp.left = binary_tree(key)
                break
            else:
                q.append(temp.left)

            if (not temp.right):
                temp.right = binary_tree(key)
                break
            else:
                q.append(temp.right)


if __name__=='__main__':
    rootdata = int(input("Enter data :"))
    bt = binary_tree(rootdata)
    c=0
    while (c != 5):
        print("\n1.PrintTree"
              "\n2.Add data"
              "\n3.Nodes in tree"
              "\n5.Exit\n")
        c = int(input("Enter choice : "))
        if c == 1:
            i = 0
            while (i != 4):
                print("1.Inorder print"
                      "\n2.Postorder print"
                      "\n3.Preorder print"
                      "\n4.Back")
                i = int(input("Enter Choice :"))
                if i == 1:
                    bt.printInorder(bt)
                    print("\n")
                elif i == 2:
                    bt.printPostorder(bt)
                    print("\n")
                elif i == 3:
                    bt.printPreorder(bt)
                    print("\n")
                elif i == 4:
                    break
                else:
                    print("Invalid input !")

        elif c == 2:
            a=int(input("Enter data in tree :"))
            bt.insert(bt,a)

        elif c == 3:
            c = 0
            print("Nodes in tree : ", bt.Nodes_in_tree())
        elif c == 5:
            break
        else:
            print("Wrong input ")

        