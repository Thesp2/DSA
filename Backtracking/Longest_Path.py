def longestpath(mat,i,j,di,dj,n,m,cur=0,ans=-1):
    if i==di and j==dj:
        if cur>ans:
            ans=cur
        return ans
    
    if mat[i][j]==0 or mat[di][dj]==0:
        return ans
    
    mat[i][j]=0

    if j!=m-1 and mat[i][j+1]>0:
        ans=longestpath(mat,i,j+1,di,dj,n,m,cur+1,ans)
    if j!=0 and mat[i][j-1]>0:
        ans=longestpath(mat,i,j-1,di,dj,n,m,cur+1,ans)
    if i!=n-1 and mat[i+1][j]>0:
        ans=longestpath(mat,i+1,j,di,dj,n,m,cur+1,ans)
    if i!=0 and mat[i-1][j]>0:
        ans=longestpath(mat,i-1,j,di,dj,n,m,cur+1,ans)

    mat[i][j]=1

    return ans

mat = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
print("Longest path will be:",longestpath(mat,0,0,2,3,len(mat),len(mat[0])))