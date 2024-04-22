class Node:
     def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        self.hd=0
def level_order(root,order='TB'):
    l={}
    q=[(root,0)]
    while q:
        node,lvl=q.pop(0)
        if lvl not in l:
            l[lvl]=[]
        l[lvl].append(node.data)
        if node.left:
            q.append((node.left,lvl-1))
        if node.right:
            q.append((node.right,lvl+1))
    
        if order =='TB':
            print("\n level order:")
        
            for lvl in l:
                 print(l[lvl],end=",")
        elif order=='BT':
            print("\n reverselevel:")
            for lvl in sorted(l,reverse=True):
                print(l[lvl],end=",")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
root=Node('a')
root.left=Node('b')
root.right=Node('c')
root.left.left=Node('d')
root.left.right=Node('e')
root.right.left=Node('f')
root.right.right=Node('g')
level_order(root,"BT")

