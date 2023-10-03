adj_list = {
 'A' : ['B','C'],
 'B' : ['D','E'],
 'C' : ['E','F'],
 'D' : ['G','B'],
 'E' : ['B','C'],
 'F' : ['C','H'],
 'G' : ['I'],
 'I' : ['J'],
 'H' : ['K'],
 'K' : ['L'],
 'L' : ['M'],
 'M' : ['N'],                    
 'J' : [],
 'N' : [],
}
label={
    'A':[0,0],
    'B':[0,3], 
    'C':[4,0], 
    'D':[3,0], 
    'E':[4,3], 
    'F':[1,3],
    'G':[3,3],
    'H':[1,0],
    'I':[4,2],
    'J':[0,2],
    'K':[0,1],
    'L':[4,1],
    'M':[2,3],
    'N':[2,0]
}
traversal_path = []
visited = [] # List to keep track of visited nodes.
stack = [] #Initialize a queue
def dfs(adj_list, start, target, path):
    stack.append(start) 
    while stack:
        s = stack.pop()
        print (s, end = " ")
        print(label[s],end = " ")
        path.append(s) # to create path list 
        visited.append(s) #all vistied node
        if s == target:
            return path 
        for neighbour in adj_list[s]:
            if neighbour not in visited:
                stack.append(neighbour)           
traversal_path=dfs(adj_list, 'A', 'N',traversal_path)
print(traversal_path)
