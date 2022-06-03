### Graph Algorithms
#### Breadth First Search (BFS)
##### Technique: Queue
<pre>
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


#### Depth First Search (DFS)
##### Technique: Queue

<pre>
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
