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
