#Sorting tuples using the second element

def sortTuples(students):
    students = students.sort(key = lambda x : x[1])
    return students
    
