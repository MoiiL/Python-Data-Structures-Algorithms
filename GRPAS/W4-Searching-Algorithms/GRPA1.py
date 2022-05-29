def neighbours(Amat,v):
    (rows,cols) = (len(Amat),len(Amat[0]))
    nbrs = []
    for i in range(cols):
        if Amat[i][v] == 1:
            nbrs.append(i)
    return nbrs
    
def findConnectionLevel(v,Amat, X, Y):
    level = {}
    (rows,cols) = (len(Amat),len(Amat[0]))
    for i in range(rows):
        level[i] = -1
    q = []
    q.append(X)
    level[X] = 0
    
    while q != []:
        j = q.pop()
        for k in neighbours(Amat,j):
            
            if k == Y:
                level[k] = level[j]+1
                break
            
            if level[k] == -1:
                level[k] = level[j]+1
                q.append(k)
            
    
    if level[Y] >= 0:
        return level[Y]
    else:
        return 0


vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))
