edge_list=[('a','b',2),('b','d',4),('d','e',5),('c','e',1),('c','d',6),('a','c',3)]
tot=0
for edge in edge_list:
    tot+=edge[2]
v_set=set()
for edge in edge_list:
    v_set.add(edge[0])
    v_set.add(edge[1])
print("no_of_node",len(v_set))
'''print("tot dist=",tot)'''
adj_list={v:[] for v in v_set}
for edge in edge_list:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])
print("adj list:",adj_list)
print("tot dist=",tot)
