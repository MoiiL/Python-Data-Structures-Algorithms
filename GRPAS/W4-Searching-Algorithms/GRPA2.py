def DFSInitGlobal(ls):
    visit = {}
    for i in ls.keys():
        visit[i] = False
    return visit
    

def DFSGlobal(ls,visit,v):
    visit[v] = True
    for k in ls[v]:
        if not visit[k]:
            DFSGlobal(ls, visit, k)
    return visit
    
    
def findMasterTank(v,e):
    n = len(v)
    ls = {}
    for i in range(int(v[0]), int(v[-1])+1):
        ls[i] = []
    for (i,j) in e:
        ls[int(i)].append(int(j))
    DFSInitGlobal(ls)
    for i in ls.keys():
        visit = DFSGlobal(ls, DFSInitGlobal(ls),i)
        Flag = True
        for k in visit.keys():
            if visit[k] != True:
                Flag = False
                break
        if Flag:
            return i 
    return 0





v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))
