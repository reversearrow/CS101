#AntiSymmetric


def antisymmetric(A):
    j = 0
    i = 0
    while i < len(A):
        while j < len(A):
            
            
            print A[i][j] , A[j][i]
            if A[i][j] != - A[j][i]:
                return False
                
            
            
            j += 1
        i = i + 1
        j = 0
    return True
    

def is_identity_matrix(matrix):
    j = 0
    count = 0
    for i in matrix:
        for k in i:
            if k != 1:
                if k != 0:
                    count = count + 1

        if i[j] != 1:
            return False 
        print count 
        if count > 0:
            return False
        j += 1
        count = 0

    return True


matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]       


matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]
