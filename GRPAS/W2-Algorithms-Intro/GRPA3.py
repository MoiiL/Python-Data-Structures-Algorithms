#Using swapping method to arrange two lists

def mergeInPlace(lsA,lsB):
    nA,nB = len(lsA),len(lsB)
    j = 0
    for i in range(nA):
        for j in range(nB):
            if(lsA[i]>lsB[j]):
                lsA.swap(i,lsB,j)
    for i in range(nB):
        for j in range(i+1,nB):
            if(lsB[i]>lsB[j]):
                lsB.swap(i,lsB,j)
                
                
