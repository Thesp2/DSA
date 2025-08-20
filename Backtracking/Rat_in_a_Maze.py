direction="DLRU"

dr=[1,0,0,-1]
dc=[0,-1,1,0]

def isvalid(row,col,n,maze):
    return 0<=row<n and 0<=col<n and maze[row][col]==1

def path(row,col,n,maze,ans,currentpath):
    if row==n-1 and col==n-1:
        ans.append(currentpath) 
        return 
    
    maze[row][col]=0
    for i in range(4):
        nextrow=row+dr[i]
        nextcol=col+dc[i]
        if isvalid(nextrow,nextcol,n,maze):
            currentpath+=direction[i]
            path(nextrow,nextcol,n,maze,ans,currentpath)
            currentpath=currentpath[:-1]
        
    maze[row][col]=1

def ratmaze(maze):
    n=len(maze)
    result=[]
    currentpath=""

    if maze[0][0]!=0 and maze[n-1][n-1]!=0:
        path(0,0,n,maze,result,currentpath)

    if not result:
        return -1
    else:
        return result
    
maze=[[1,0,0,0],
      [1,1,1,0],
      [1,1,0,0],
      [1,1,1,1]]
print(ratmaze(maze))