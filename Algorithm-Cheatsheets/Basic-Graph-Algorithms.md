### Graph Algorithms
#### Note:
##### Sum of Degrees : 2m ( m represents the number of edges)
#### Breadth First Search (BFS)

<ul>
  <li>BFS with adjacency matrix : Overall time O(n<sup>2</sup>) </li>
  <li>BFS with adjacency list : Overall time (Amortized complexity) O(n + m) </li>
  </ul>

##### Technique: Queue
<pre>
Code I
<p>
  class Queue:
      def __init__ (self):
          self.queue = []
      
      def addqueue(self,ele):
          self.queue.append(ele)
      
      def deletequeue(self):
          ele = None
          if not self.isempty():
               ele = self.queue[0]
               self.queue = self.queue[1:]
          return (ele)
  
      def isempty(self):
          return (self.queue == [])
  
      def __str__ (self):
          return (str(self.queue))
</p>
</pre>

<pre>
Code II
<p>
def BFSListPath(ls,ele):
   (visited, parent) = ({},{})
   for i in ls.keys():
       visited[i] = False
       parent[i] = -1
   q = Queue()
   
   visited[ele] = True
   q.addqueue(ele)
   
   while(not q.isempty()):
        j = q.deletequeue()
        for k in ls[j]:
            if (not visited[k]):
                 visited[k] = True
                 parent[k] = j
                 q.addqueue(k)
   return (visited, parent)
</p>
</pre>

<pre>
Code III
<p>
def BFS(matrix, ele):
    (rows, cols) = matrix.shape
    visited = {}
    for i in range(rows):
        visited[i] = False
    q = Queue()
    
    visited[ele] = True
    q.addqueue(ele)
    
    while (not q.isempty()):
         j = q.deletequeue()
         for k in neighbours(matrix,j):
             if (not visited[k]):
                 visited[k] = True
                 q.addqueue(k)
                 
    return (visited)
</p>
</pre>


#### Depth First Search (DFS)
##### Technique: Stack
###### Note:
<ul>
  <li> Overall time for adjacency matrix: O(n<sup>2</sup>)</li>
  <li> Overall time for adjacency list: O(n+m)</li>
  </ul>

<pre>
Code I
<p>
def DFSinitialise(mat):
   (rows, cols) = mat.shape
   (visited, parent) = ({}, {})
   for i in range(rows):
       visited[i] = False
       parent[i] = -1
   return (visited, parent)
   
def DFS(mat, visited, parent, ele):
    visited[ele] = True
    for k in neighbours(mat,v):
       if (not visited[k]):
          parent[k] = v
          (visited, parent) = DFS(mat, visited, parent, k)
    return (visited, parent)
</p>
</pre>

<pre>
Code II
<p>
(visited, parent) = ({}, {})

def DFSinitialiseglobal(mat):
    (rows, cols) = mat.shape
    for i in range(rows):
         visited[i] = False
         parent[i] = -1
    return
    
def DFSglobal(mat, v):
    visited[v] = True
    
    for k in neighbours(mat, v):
       if not visited[k]:
           parent[k] = v
           DFSglobal(mat, v)
    return

     
</p>
</pre>
