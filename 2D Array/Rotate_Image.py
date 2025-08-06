def rotateimage(mat):
    l,r=0,len(mat)-1

    while l<r:
        for i in range(r-l):
            top,bottom=l,r

            topleft=mat[top][l+i]

            mat[top][l+i]=mat[bottom-i][l]
            mat[bottom-i][l]=mat[bottom][r-i]
            mat[bottom][r-i]=mat[top+i][r]
            mat[top+i][r]=topleft
        l+=1
        r-=1

matrix=[[1,2,3,8],
        [4,5,6,8],
        [7,8,9,8],
        [1,1,1,8]]
rotateimage(matrix)
for i in matrix:
    print(i)            