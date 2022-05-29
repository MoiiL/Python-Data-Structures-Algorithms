def longJourney(Alist):
    visited = {}
    for i in Alist.keys():
        visited[i] = False
    
    cities = []
    def DFS(s,path):
        visited[s] = True
        if path == []:
            path.append(s)
        for k in Alist[s]:
            if not visited[k]:
                DFS(k,path+[k])
        path.append(s)
        cities.append(path)
        path.pop()
        visited[s] = False
        
    
    DFS('Leh',path=[])
    max = 0
    index = 0
    for i in range(len(cities)):
        if len(cities[i]) > max:
            max = len(cities[i])
            index = i
    return cities[index]
