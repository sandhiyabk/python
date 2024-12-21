def adjacencylist(v,edges):
    adj=[[] for _ in range(v+1)]
    for edge in edges:
        u,v=edge
        adj[u].append(v)
        adj[v].append(u)
    return adj
v=4
edges=[(1,2),(2,3),(3,0),(0,1)]
adj_list=adjacencylist(v,edges)
for i in range(v) :
    print(f"{i}->{adj_list[i]}")
