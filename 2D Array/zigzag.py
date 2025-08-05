def zigzag(mat):
    rows=len(mat)
    col=len(mat[0])
    res=[]

    for d in range(rows+col-1):
        temp=[]
        for i in range(rows):
            j=d-i
            if 0<=j<col:
                temp.append(mat[i][j])
        
        
        temp.reverse()
        res.extend(temp)
    
    return res

matrix=[[ 1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]]
print(zigzag(matrix))