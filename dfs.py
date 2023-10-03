#DFS
adj_list = {
 'A' : ['B','C'],
 'B' : ['D', 'E'],
 'C' : ['F','G'],
 'D' : [],
 'E' : [ ],
 'F' : ['C'],
 'G' : ['B','D']
}
label={
    'A':[0,0], 'B':[0,3], 'C':[4,0], 'D':[3,0], 'E':[4,3], 'F':[1,3], 'G':[3,3]
}
traversal_path = []
visited = [] # List to keep track of visited nodes.
stack = [] #Initialize a queue
def dfs(adj_list, start, target, path):
    stack.append(start) 
    while stack:
        s = stack.pop(0)
        print (s, end = " ")
        print(label[s],end = " ")
        path.append(s) # to create path list 
        visited.append(s) #all vistied node
        if s == target:
            return path
        for neighbour in adj_list[s]:
            if neighbour not in visited:
                stack.append(neighbour) # all child of out node has been pushed
dfs(adj_list, 'A', 'F',traversal_path)
