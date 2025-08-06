def set_zero(mat):
    rows=len(mat)
    col=len(mat[0])
    zero_col=False
    
    for i in range(rows):
        if mat[i][0]==0:
            zero_col=True
        for j in range(1,col):
            if mat[i][j]==0:
                mat[i][0]=0
                mat[0][j]=0
        
    for i in range(1,rows):
        for j in range(1,col):
            if mat[i][0]==0 or mat[0][j]==0:
                mat[i][j]=0
                
    if mat[0][0]==0:
        for j in range(col):
            mat[0][j]=0
            
    if zero_col:
        for i in range(rows):
            mat[i][0]=0

matrix=[[1,2,3],[1,0,3],[1,2,3]]
set_zero(matrix)
for row in matrix:
    print(row)