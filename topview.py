class Node:
    def __init__(self,d):
        self.lc=None
        self.rc=None
        self.d=d
        self.hd=0
    def constructTree(nodelist):
        root=Node(nodelist[0])
        root.lc=Node(nodelist[1])
        root.rc=Node(nodelist[2])
        root.lc.lc=Node(nodelist[3])
        root.lc.rc=Node(nodelist[4])
        root.rc.lc=Node(nodelist[5])
        root.rc.rc=Node(nodelist[6])
        return root
    def Topview(root):
        m={}
        q=[]
        q=[root]
        while len(q)>0:
            cur_node=q.pop(0)
            if cur_node.hd not in m:
                m[cur_node.hd]=cur_node.d
            if cur_node.lc:
                cur_node.lc.hd=cur_node.hd-1
                q.append(cur_node.lc)
            if cur_node.rc:
                cur_node.rc.hd=cur.node.hd+1
                q.append(cur.node.rc)
        m=sort(m)
        print("top[ view")
        for k,v in m.items():
            print(v,end=",")
nodelist=['A','B','C','D','E','F','G']
root=    constructTree(nodelist)
Topview(root)
