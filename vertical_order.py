class Node:
     def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        self.hd=0
def vertical_order(root):
    l={}
    q=[(root,0)]
    while q:
        node,hd=q.pop(0)
        if hd not in l:
            l[hd]=[]
        l[hd].append(node.data)
        if node.left:
            q.append((node.left,hd-1))
        if node.right:
            q.append((node.right,hd+1))
    print ("level")
    for hd in l:
        print(l[hd],end=",")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
root=Node('a')
root.left=Node('b')
root.right=Node('c')
root.left.left=Node('d')
root.left.right=Node('e')
root.right.left=Node('f')
root.right.right=Node('g')
vertical_order(root)

