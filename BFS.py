#BFS
graph = {
 'A' : ['B','C'],
 'B' : ['D', 'E'],
 'C' : ['F','G'],
 'D' : [],
 'E' : [ ],
 'F' : ['C'],
 'G' : ['B','D'],
 
}

label={
    'A':[0,0], 'B':[0,3], 'C':[4,0], 'D':[3,0], 'E':[4,3], 'F':[1,3], 'G':[3,3]
}

visited = [] # List to keep track of visited nodes.
queue = [] #Initialize a queue
def bfs(visited, graph, node):
 visited.append(node)
 queue.append(node)
 while queue:
    s = queue.pop(0)
    print (s, end = " ")
    print(label[s],end = " ")
    if s in goal:
        return
    for neighbour in graph[s]:
        if neighbour not in visited:
           visited.append(neighbour)
           queue.append(neighbour)
# Driver Code
bfs(visited, graph, 'A')
